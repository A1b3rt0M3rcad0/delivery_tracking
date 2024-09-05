from controllers.contracts import PostInputCreateContract, PostInputSelectContract, PostInputDeleteContract, PostInputUpdateContract
from controllers.contracts import DeliveryStepInputCreateContract, DeliveryStepInputDeleteContract, DeliveryStepInputSelectContract, DeliveryStepInputUpdateContract
from controllers.controllers import PostController, DeliveryStepController
from datetime import date
from typing import List, Dict, Any, Tuple

class PostService:

    post_controller = PostController()
    

    def _create_post(self, delivery_code: str, addresse_name: str, full_address: str, created_at: date, finished: bool) -> Tuple[bool | date]:
        # Cria uma instância do contrato com os dados fornecidos
        contract = PostInputCreateContract(
            delivery_code=delivery_code,
            addresse_name=addresse_name,
            full_address=full_address,
            created_at=created_at,
            finished=finished
        )
        # Obtém os parâmetros do contrato e chama o método apropriado no controlador
        params = contract.get_params()
        result = self.post_controller.create(**params)
        return (result, created_at)
    
    def _select_post(self, delivery_code:str) -> List[object]:
        # Cria uma instância do contrato com os parâmetros de seleção
        contract = PostInputSelectContract(delivery_code=[delivery_code])
        # Obtém os parâmetros do contrato e chama o método apropriado no controlador
        params = contract.get_params()
        result = self.post_controller.select(**params)
        return result

class DeliveryStepService:

    delivery_step_controller = DeliveryStepController()
    
    def _create_delivery_step(self, delivery_steps:List[Dict[str, Any]]) -> List[bool]:
        # Cria a lista de contratos que serão adicionados
        contracts = []
        for i, delivery_step in enumerate(delivery_steps):
            if i == 0:
                contract = DeliveryStepInputCreateContract(**delivery_step)
                contracts.append(contract)
            else:
                finished_at = contracts[-1].get_params().get('finished_at')
                delivery_step['started_at'] = finished_at
                contract = DeliveryStepInputCreateContract(**delivery_step)
                contracts.append(contract)
        
        results = []
        # Criando delivery_steps
        for contract in contracts:
            result = self.delivery_step_controller.create(**contract.get_params())
            results.append(result)
    
        return results
    
    def _select_delivery_steps(self, delivery_code:str) -> List[object]:
        # Cria uma instância do contrato com os parâmetros de seleção do post
        post_service = PostService()
        post_contract = PostInputSelectContract(delivery_code=delivery_code)
        result_post_query = post_service._select_post(**post_contract.get_params())
        post_id = result_post_query[0].id
        # Cria uma instância do contrato de delivery step e coleta os steps pelo id do post
        delivery_step_contract = DeliveryStepInputSelectContract(post_id=[post_id])
        result_delivery_step_query = self.delivery_step_controller.select(**delivery_step_contract.get_params())
        return result_delivery_step_query
