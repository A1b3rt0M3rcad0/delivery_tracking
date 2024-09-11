from config.config import Config
from routes.routes import r

app = Config.app

app.run(debug=True)