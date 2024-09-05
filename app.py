from services.services import PostService
from datetime import date, timedelta


post_service = PostService()

post = post_service._create_post(
    'UIAHSDUHAIUSHD',
    'Orleans',
    'Calabouco aushdiuas',
    date.today(),
    False,
)

post = post_service._create_delivery_step(
    [{
        'post_id': 1,
        'delivery_stage_name': 'Separação',
        'delivery_stage_description': 'Tunel',
        'delivery_stage': 4,
        'due_date_delivery_stage': 5,
        'started_at': date.today(),
        'finished': False
    
    },
    {
        'post_id': 1,
        'delivery_stage_name': 'Separação',
        'delivery_stage_description': 'Tunel',
        'delivery_stage': 5,
        'due_date_delivery_stage': 5,
        'finished': False
    
    }]
)

print(post)