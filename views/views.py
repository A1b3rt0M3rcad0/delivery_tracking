from flask import url_for, render_template, redirect, request
from services.services import MainService

main_service = MainService()

def home():
    return render_template('home.html', page_title='Home')


def tracking():
    tracking_code = request.args['tracking_code']
    response = main_service.get_full_report(tracking_code)
    print(response)
    return f'Hello {response.get('post')[0].delivery_code}'
