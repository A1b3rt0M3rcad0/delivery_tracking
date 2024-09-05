from services.services import PostService, DeliveryStepService
from datetime import date, timedelta


post_service = PostService()
delivery_step_service = DeliveryStepService()

# post = post_service._create_post(
#     'UIAHSDUHAIUSHD',
#     'Orleans',
#     'Calabouco aushdiuas',
#     date.today(),
#     False,
# )

# post = delivery_step_service._create_delivery_step(
#     [{
#         'post_id': 1,
#         'delivery_stage_name': 'Separação',
#         'delivery_stage_description': 'Tunel',
#         'delivery_stage': 7,
#         'due_date_delivery_stage': 3,
#         'started_at': date.today(),
#         'finished': False
    
#     },
#     {
#         'post_id': 1,
#         'delivery_stage_name': 'Separação',
#         'delivery_stage_description': 'Tunel',
#         'delivery_stage': 8,
#         'due_date_delivery_stage': 5,
#         'finished': False
    
#     }]
# )

t = delivery_step_service._select_delivery_steps('UIAHSDUHAIUSHD')

print(t)