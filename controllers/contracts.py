from typing import Any, Dict, Optional, List
from controllers.base.base_input import BaseInputContract
from datetime import date, timedelta

#### POST CONTRACTS ################################################################################################################################################

class PostInputCreateContract(BaseInputContract):

    def __init__(self, delivery_code:str, addresse_name:str, full_address:str, created_at:date, finished:bool) -> None:
        super().__init__()
        self.delivery_code = delivery_code
        self.addresse_name = addresse_name
        self.full_address = full_address
        self.created_at = created_at
        self.finished = finished

    def get_params(self) -> Dict[str, Any]:
        params = {
            'delivery_code': self.delivery_code,
            'addresse_name': self.addresse_name,
            'full_address': self.full_address,
            'created_at': self.created_at,
            'finished': self.finished
        }
        return params

class PostInputSelectContract(BaseInputContract):
    """Classe para contratos de input para operações de seleção em controladores de Post."""

    def __init__(self, 
                 delivery_code: Optional[List[str]] = None,
                 addresse_name: Optional[List[str]] = None,
                 full_address: Optional[List[str]] = None,
                 created_at: Optional[List[date]] = None,
                 finished: Optional[List[bool]] = None) -> None:
        super().__init__()
        self.delivery_code = delivery_code
        self.addresse_name = addresse_name
        self.full_address = full_address
        self.created_at = created_at
        self.finished = finished

    def get_params(self) -> Dict[str, Any]:
        params = {
            'delivery_code': self.delivery_code,
            'addresse_name': self.addresse_name,
            'full_address': self.full_address,
            'created_at': self.created_at,
            'finished': self.finished
        }
        # Remove keys with None values
        return self.clean_params(params)

class PostInputDeleteContract(BaseInputContract):
    """Classe para contratos de input para operações de exclusão em controladores de Post."""

    def __init__(self, 
                 delivery_code: Optional[List[str]] = None,
                 addresse_name: Optional[List[str]] = None,
                 full_address: Optional[List[str]] = None,
                 created_at: Optional[List[date]] = None,
                 finished: Optional[List[bool]] = None) -> None:
        super().__init__()
        self.delivery_code = delivery_code
        self.addresse_name = addresse_name
        self.full_address = full_address
        self.created_at = created_at
        self.finished = finished

    def get_params(self) -> Dict[str, Any]:
        params = {
            'delivery_code': self.delivery_code,
            'addresse_name': self.addresse_name,
            'full_address': self.full_address,
            'created_at': self.created_at,
            'finished': self.finished
        }
        return self.clean_params(params)

class PostInputUpdateContract(BaseInputContract):
    """Classe para contratos de input para operações de atualização em controladores de Post."""

    def __init__(self, 
                 delivery_code: Optional[str] = None,
                 addresse_name: Optional[str] = None,
                 full_address: Optional[str] = None,
                 created_at: Optional[date] = None,
                 finished: Optional[bool] = None,
                 filters: Optional[Dict[str, List[Any]]] = None) -> None:
        """
        Inicializa um contrato de input para atualização de registros.

        Args:
            delivery_code (Optional[str]): Código de entrega.
            addresse_name (Optional[str]): Nome do destinatário.
            full_address (Optional[str]): Endereço completo.
            created_at (Optional[date]): Data de criação.
            finished (Optional[bool]): Status de finalização.
            filters (Optional[Dict[str, List[Any]]]): Filtros para selecionar registros a serem atualizados.
        """
        super().__init__()
        self.delivery_code = delivery_code
        self.addresse_name = addresse_name
        self.full_address = full_address
        self.created_at = created_at
        self.finished = finished
        self.filters = filters

    def get_params(self) -> Dict[str, Any]:
        """
        Retorna os parâmetros do contrato de atualização.

        Returns:
            Dict[str, Any]: Dicionário com os valores a serem atualizados.
        """
        params = {
            'delivery_code': self.delivery_code,
            'addresse_name': self.addresse_name,
            'full_address': self.full_address,
            'created_at': self.created_at,
            'finished': self.finished
        }
        # Remove keys with None values
        return self.clean_params(params)

    def get_filters(self) -> Dict[str, List[Any]]:
        """
        Retorna os filtros para selecionar os registros a serem atualizados.

        Returns:
            Dict[str, List[Any]]: Dicionário com os filtros de seleção.
        """
        return self.filters or {}

##################################################################################################################################################################

#### DELIVERYSTEP CONTRACTS ################################################################################################################################################

class DeliveryStepInputCreateContract(BaseInputContract):

    def __init__(self, post_id:int, delivery_stage_name:str, delivery_stage_description:str, delivery_stage:int, due_date_delivery_stage:int, started_at:date, finished:bool) -> None:
        super().__init__()
        self.post_id = post_id
        self.delivery_stage_name = delivery_stage_name
        self.delivery_stage_description = delivery_stage_description
        self.delivery_stage = delivery_stage
        self.due_date_delivery_stage = due_date_delivery_stage
        self.started_at = started_at
        self.finished = finished

    def get_params(self) -> Dict[str, Any]:
        params = {
            'post_id': self.post_id,
            'delivery_stage_name': self.delivery_stage_name,
            'delivery_stage_description': self.delivery_stage_description,
            'delivery_stage': self.delivery_stage,
            'due_date_delivery_stage': self.due_date_delivery_stage,
            'started_at': self.started_at,
            'finished_at': self.started_at + timedelta(days=self.due_date_delivery_stage),
            'finished': self.finished
        }
        return params

class DeliveryStepInputSelectContract(BaseInputContract):
    """Classe para contratos de input para operações de seleção em controladores de DeliveryStep."""

    def __init__(self,
                 post_id:Optional[List[int]] = None, 
                 delivery_stage_name:Optional[List[str]] = None, 
                 delivery_stage_description:Optional[List[str]] = None, 
                 delivery_stage:Optional[List[int]] = None, 
                 due_date_delivery_stage:Optional[List[int]] = None, 
                 started_at:Optional[List[date]] = None, 
                 finished_at:Optional[List[date]] = None, 
                 finished:Optional[List[bool]] = None) -> None:
        super().__init__()
        self.post_id = post_id
        self.delivery_stage_name = delivery_stage_name
        self.delivery_stage_description = delivery_stage_description
        self.delivery_stage = delivery_stage
        self.due_date_delivery_stage = due_date_delivery_stage
        self.started_at = started_at
        self.finished_at = finished_at
        self.finished = finished

    def get_params(self) -> Dict[str, Any]:
        params = {
            'post_id': self.post_id,
            'delivery_stage_name': self.delivery_stage_name,
            'delivery_stage_description': self.delivery_stage_description,
            'delivery_stage': self.delivery_stage,
            'due_date_delivery_stage': self.due_date_delivery_stage,
            'started_at': self.started_at,
            'finished_at': self.finished_at,
            'finished': self.finished
        }
        # Remove keys with None values
        return self.clean_params(params)

class DeliveryStepInputDeleteContract(BaseInputContract):
    """Classe para contratos de input para operações de exclusão em controladores de DeliveryStep."""

    def __init__(self,
                 post_id:Optional[List[int]] = None, 
                 delivery_stage_name:Optional[List[str]] = None, 
                 delivery_stage_description:Optional[List[str]] = None, 
                 delivery_stage:Optional[List[int]] = None, 
                 due_date_delivery_stage:Optional[List[int]] = None, 
                 started_at:Optional[List[date]] = None, 
                 finished_at:Optional[List[date]] = None, 
                 finished:Optional[List[bool]] = None) -> None:
        super().__init__()
        self.post_id = post_id
        self.delivery_stage_name = delivery_stage_name
        self.delivery_stage_description = delivery_stage_description
        self.delivery_stage = delivery_stage
        self.due_date_delivery_stage = due_date_delivery_stage
        self.started_at = started_at
        self.finished_at = finished_at
        self.finished = finished

    def get_params(self) -> Dict[str, Any]:
        params = {
            'post_id': self.post_id,
            'delivery_stage_name': self.delivery_stage_name,
            'delivery_stage_description': self.delivery_stage_description,
            'delivery_stage': self.delivery_stage,
            'due_date_delivery_stage': self.due_date_delivery_stage,
            'started_at': self.started_at,
            'finished_at': self.finished_at,
            'finished': self.finished
        }
        return self.clean_params(params)

class DeliveryStepInputUpdateContract(BaseInputContract):
    """Classe para contratos de input para operações de atualização em controladores de DeliveryStep."""

    def __init__(self,
                 post_id:Optional[List[int]] = None, 
                 delivery_stage_name:Optional[List[str]] = None, 
                 delivery_stage_description:Optional[List[str]] = None, 
                 delivery_stage:Optional[List[int]] = None, 
                 due_date_delivery_stage:Optional[List[int]] = None, 
                 started_at:Optional[List[date]] = None, 
                 finished_at:Optional[List[date]] = None, 
                 finished:Optional[List[bool]] = None,
                 filters: Optional[Dict[str, List[Any]]] = None) -> None:
        """
        Inicializa um contrato de input para atualização de registros.

        Args:
            post_id (Optional[int]): ID do post relacionado.
            delivery_stage_name (Optional[str]): Nome da etapa de entrega.
            delivery_stage_description (Optional[str]): Descrição da etapa de entrega.
            delivery_stage (Optional[int]): Número da etapa de entrega.
            due_date_delivery_stage (Optional[int]): Data de vencimento da etapa de entrega.
            started_at (Optional[date]): Data de início.
            finished_at (Optional[date]): Data de finalização.
            finished (Optional[bool]): Status de finalização.
            filters (Optional[Dict[str, List[Any]]]): Filtros para selecionar registros a serem atualizados.
        """
        super().__init__()
        self.post_id = post_id
        self.delivery_stage_name = delivery_stage_name
        self.delivery_stage_description = delivery_stage_description
        self.delivery_stage = delivery_stage
        self.due_date_delivery_stage = due_date_delivery_stage
        self.started_at = started_at
        self.finished_at = finished_at
        self.finished = finished
        self.filters = filters

    def get_params(self) -> Dict[str, Any]:
        """
        Retorna os parâmetros do contrato de atualização.

        Returns:
            Dict[str, Any]: Dicionário com os valores a serem atualizados.
        """
        params = {
            'delivery_stage_name': self.delivery_stage_name,
            'delivery_stage_description': self.delivery_stage_description,
            'delivery_stage': self.delivery_stage,
            'due_date_delivery_stage': self.due_date_delivery_stage,
            'started_at': self.started_at,
            'finished_at': self.finished_at,
            'finished': self.finished
        }
        # Remove keys with None values
        return self.clean_params(params)

    def get_filters(self) -> Dict[str, List[Any]]:
        """
        Retorna os filtros para selecionar os registros a serem atualizados.

        Returns:
            Dict[str, List[Any]]: Dicionário com os filtros de seleção.
        """
        return self.filters or {}

##################################################################################################################################################################