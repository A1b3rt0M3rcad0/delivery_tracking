import json

# Função para gerar o código de entrega
def gerar_codigo_entrega():
    import random
    import string
    prefixo = "BR"
    sufixo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return f"{prefixo}-{sufixo}"

# Função para serializar objetos de modelo para dict
def serialize_post(post):
    return {
        'delivery_code': post.delivery_code,
        'addresse_name': post.addresse_name,
        'full_address': post.full_address,
        'id': post.id,
        'finished': post.finished,
        'created_at': post.created_at.isoformat()  # Converte datetime para string
    }

def serialize_delivery_step(step):
    return {
        'post_id': step.post_id,
        'delivery_stage_name': step.delivery_stage_name,
        'delivery_stage': step.delivery_stage,
        'started_at': step.started_at.isoformat(),  # Converte datetime para string
        'finished': step.finished,
        'delivery_stage_description': step.delivery_stage_description,
        'id': step.id,
        'due_date_delivery_stage': step.due_date_delivery_stage,
        'finished_at': step.finished_at.isoformat()  # Converte datetime para string
    }