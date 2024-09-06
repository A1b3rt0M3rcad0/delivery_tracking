from services.services import PostService, DeliveryStepService, MainService
from datetime import date, timedelta


def main():
    # Instancia o serviço principal
    main_service = MainService()
    
    # Dados para criar um post
    post_data = {
        'addresse_name': 'Endereço Exemplo',
        'full_address': 'Rua das Flores, 123, Centro',
        'created_at': date(2024, 9, 5),
        'finished': False
    }
    
    # Dados para criar os passos de entrega
    delivery_steps = [
        {
            'delivery_stage_name': 'Passo 1',
            'delivery_stage': 0,
            'due_date_delivery_stage': 1,
            'delivery_stage_description': 'Inicio',
            'finished': False,
            'started_at': date.today(),
        },
        {
            'delivery_stage_name': 'Passo 2',
            'delivery_stage': 1,
            'due_date_delivery_stage': 1,
            'delivery_stage_description': 'Inicio',
            'finished': False,
        },
    ]
    
    # Cria um post e passos de entrega
    delivery_code, post_result, delivery_steps_result = main_service.create_post_with_delivery_steps(post_data, delivery_steps)
    
    if post_result:
        print("Post criado com sucesso!")
        print(f"Status dos passos de entrega: {delivery_steps_result}")
    else:
        print("Erro ao criar o post.")
    
    # Obtém o relatório completo
    report = main_service.get_full_report(delivery_code)
    
    if report:
        print("Relatório completo:")
        print(report)
    else:
        print("Nenhum dado encontrado para o código de entrega fornecido.")
    
    # Verifica e atualiza o status dos passos de entrega
    main_service.finished_delivery_steps_check_update(delivery_code)
    print(f"Status atualizado para o código de entrega: {delivery_code}")

if __name__ == "__main__":
    main()