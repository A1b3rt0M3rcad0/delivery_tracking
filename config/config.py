from dataclasses import dataclass
from flask import Flask

@dataclass
class Config():

    engine = 'sqlite:///db/entregas.db'
    app = Flask(__name__, static_folder='../static', template_folder='../templates')