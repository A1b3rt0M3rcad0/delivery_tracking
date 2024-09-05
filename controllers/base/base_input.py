from typing import Dict, Any

class BaseInputContract:
    """Classe base para contratos de input para operações em controladores."""
    
    def get_params(self) -> Dict[str, Any]:
        """Retorna os parâmetros necessários para uma operação criação."""
        raise NotImplementedError("Subclasse deve implementar o método 'get_params'.")
    
    def clean_params(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Remove parâmetros com valores None."""
        return {k: v for k, v in params.items() if v is not None}