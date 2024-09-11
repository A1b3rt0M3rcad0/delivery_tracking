from flask import url_for, render_template, redirect, request
from services.services import MainService

def home():
    return render_template('home.html', page_title='Home')


def tracking():
    return 'Hello Contacts'
