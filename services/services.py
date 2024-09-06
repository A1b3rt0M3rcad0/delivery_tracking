from controllers.contracts import (
    PostInputCreateContract, PostInputSelectContract,
    PostInputDeleteContract, PostInputUpdateContract,
    DeliveryStepInputCreateContract, DeliveryStepInputDeleteContract,
    DeliveryStepInputSelectContract, DeliveryStepInputUpdateContract
)
from controllers.controllers import PostController, DeliveryStepController
from datetime import date
from typing import List, Dict, Any, Tuple
from utils.utils import gerar_codigo_entrega

class BaseService:
    def __init__(self, controller):
        self.controller = controller

    def create(self, contract) -> bool:
        params = contract.get_params()
        result = self.controller.create(**params)
        return result

    def select(self, contract) -> List[object]:
        params = contract.get_params()
        result = self.controller.select(**params)
        return result

    def update(self, contract) -> bool:
        params = contract.get_params()
        filters = contract.get_filters()
        result = self.controller.update(params, **filters)
        return result

class PostService(BaseService):
    def __init__(self):
        super().__init__(PostController())

    def create_post(self, addresse_name: str, full_address: str, created_at: date, finished: bool) -> Tuple[bool, date]:
        delivery_code = gerar_codigo_entrega()

        # Checka se o delivery code já existe
        if self.select_post([delivery_code]):
            return self.create_post(addresse_name, full_address, created_at, finished)

        contract = PostInputCreateContract(
            delivery_code=delivery_code,
            addresse_name=addresse_name,
            full_address=full_address,
            created_at=created_at,
            finished=finished
        )
        result = self.create(contract)
        return (delivery_code, created_at, result)

    def select_post(self, delivery_code: List[str]) -> List[object]:
        contract = PostInputSelectContract(delivery_code=delivery_code)
        return self.select(contract)

class DeliveryStepService(BaseService):
    def __init__(self):
        super().__init__(DeliveryStepController())

    def create_delivery_steps(self, delivery_steps: List[Dict[str, Any]]) -> List[bool]:
        contracts = []
        for i, delivery_step in enumerate(delivery_steps):
            if i > 0:
                delivery_step['started_at'] = contracts[-1].get_params().get('finished_at')
            contract = DeliveryStepInputCreateContract(**delivery_step)
            contracts.append(contract)

        results = [self.create(contract) for contract in contracts]
        return results

    def select_delivery_steps(self, delivery_code: List[str]) -> List[object]:
        post_service = PostService()
        post_contract = PostInputSelectContract(delivery_code=delivery_code)
        result_post_query = post_service.select_post(post_contract.get_params().get('delivery_code'))

        if not result_post_query:
            return []

        post_id = result_post_query[0].id
        delivery_step_contract = DeliveryStepInputSelectContract(post_id=[post_id])
        return self.select(delivery_step_contract)

class MainService:
    def __init__(self):
        self.post_service = PostService()
        self.delivery_step_service = DeliveryStepService()

    def create_post_with_delivery_steps(self, post_data: Dict[str, Any], delivery_steps: List[Dict[str, Any]]) -> Tuple[bool, List[bool]]:
        delivery_code, _, post_result = self.post_service.create_post(**post_data)
        if not post_result:
            print("Erro ao criar o post.")
            return False, []
        
        post_id = self.post_service.select_post([delivery_code])[0].id

        for delivery_step in delivery_steps:
            delivery_step['post_id'] = post_id

        delivery_steps_result = self.delivery_step_service.create_delivery_steps(delivery_steps)
        return delivery_code, post_result, delivery_steps_result

    def get_full_report(self, delivery_code: str) -> Dict[str, Any]:
        post_data = self.post_service.select_post([delivery_code])
        if not post_data:
            print(f"Nenhum post encontrado com o código de entrega: {delivery_code}.")
            return {}

        delivery_steps_data = self.delivery_step_service.select_delivery_steps([delivery_code])
        return {'post': post_data, 'delivery_steps': delivery_steps_data}
    
    def finished_delivery_steps_check_update(self, delivery_code: str) -> None:
        """
        Verifica e atualiza o status de finalização dos passos de entrega.
        :param delivery_code: Código de entrega para o qual o status será verificado.
        :return: Relatório atualizado do post e dos passos de entrega.
        """
        report = self.get_full_report(delivery_code)
        today = date.today()
        finished_steps = []

        for delivery_step in report['delivery_steps']:
            delivery_step_finished_at = delivery_step.finished_at
            if delivery_step_finished_at < today:
                contract = DeliveryStepInputUpdateContract(finished=True, filters={'id': delivery_step.id})
            else:
                contract = DeliveryStepInputUpdateContract(finished=False, filters={'id': delivery_step.id})

            # Atualiza o passo de entrega usando o contrato
            self.delivery_step_service.update(contract)
            finished_steps.append(contract.get_params().get('finished'))

        # Verifica se todos os passos de entrega foram finalizados
        if all(finished_steps):
            contract = PostInputUpdateContract(finished=True, filters={'delivery_code': delivery_code})
            self.post_service.update(contract)
        else:
            contract = PostInputUpdateContract(finished=False, filters={'delivery_code': delivery_code})
            self.post_service.update(contract)