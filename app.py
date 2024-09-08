from flask import Flask, url_for, render_template, redirect, request
from services.services import MainService

app = Flask(__name__)


# HomePage
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', page_title='Home')

@app.route('/track_order')
def track_order():
    return render_template('home.html', page_title='Home')



app.run(debug=True)