from flask import Blueprint

base_api = Blueprint('base_api_v1', __name__, url_prefix='/welcome/')

@base_api.route("/init")
def init():
    
    return "Ok",200
