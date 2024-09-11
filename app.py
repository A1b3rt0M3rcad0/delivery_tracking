from config.config import Config
from routes.routes import *

app = Config.app

app.run(debug=True)