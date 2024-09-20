from flask import url_for, render_template, redirect, request, jsonify
from services.services import MainService
import json
from utils.utils import serialize_delivery_step, serialize_post

main_service = MainService()

def home():
    return render_template('home.html', page_title='Home')


def tracking():
    tracking_code = request.args['tracking_code']
    main_service.finished_delivery_steps_check_update(tracking_code)
    response = main_service.get_full_report(tracking_code)
    
    # Serializando o post e os delivery steps
    post = [serialize_post(p) for p in response['post']]
    delivery_steps = [serialize_delivery_step(ds) for ds in response['delivery_steps']]
    
    # Criação do dicionário final a ser passado
    response_dict = {
        'post': post,
        'delivery_steps': delivery_steps
    }
    
    try:
        # Serializando o dict para JSON
        response_json = json.dumps(response_dict)
        # Redireciona com o JSON na query string
        return redirect(url_for('screening_result', response=response_json))
    except TypeError:
        return 'None'

def screening_result():
    # Recupera o JSON da query string e desserializa
    response_json = request.args.get('response')
    if response_json:
        response = json.loads(response_json)
        return render_template('result.html', context=response)  # Exibe como JSON
    return 'No response found'

