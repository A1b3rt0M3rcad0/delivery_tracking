from controllers.base.base_controller import BaseController
from models.models import DeliveryStep, Post


class PostController(BaseController):

    def __init__(self) -> None:
        super().__init__(Post)

class DeliveryStepController(BaseController):

    def __init__(self) -> None:
        super().__init__(DeliveryStep)

