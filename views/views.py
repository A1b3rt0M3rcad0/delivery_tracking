from flask import url_for, render_template, redirect, request
from services.services import MainService

def home():
    return render_template('home.html', page_title='Home')


def tracking():
    tracking_code = request.args['tracking_code']
    return f'Hello {tracking_code}'
