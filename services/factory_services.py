from flask import Flask
from routes.routes import base_api
import config
import helper.debug_message as dbg_message

def init_services():
    app = Flask(__name__)
    app.register_blueprint(base_api)
    return app
