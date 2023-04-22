from flask import Blueprint
from helper.response_helper import make_response
import constant.exception.generic_error_code_message as generic_error_code_message
from constant.database_constants import *
from singleton.redis_manager import redis_manager

base_api = Blueprint('base_api_v1', __name__, url_prefix='/api/v1/welcome/')


@base_api.route("/init")
def init():
    response = dict()
    # Android version
    response['android_version'] = redis_manager.redis_db.get(android_version_key) \
        if redis_manager.redis_db.exists(android_version_key) else ""
    # iOS version
    response['ios_version'] = redis_manager.redis_db.get(apple_version_key) \
        if redis_manager.redis_db.exists(apple_version_key) else ""

    return make_response(data=response, status_code=generic_error_code_message.no_error), 200


@base_api.route("/info")
def info():
    response = dict()
    try:
        # Last update
        response['last_update'] = redis_manager.redis_db.get(last_update_version_key) \
            if redis_manager.redis_db.exists(last_update_version_key) else ""
        # Android version
        response['android_version'] = redis_manager.redis_db.get(android_version_key) \
            if redis_manager.redis_db.exists(android_version_key) else ""
        # iOS version
        response['ios_version'] = redis_manager.redis_db.get(apple_version_key) \
            if redis_manager.redis_db.exists(apple_version_key) else ""
        return make_response(data=response, status_code=generic_error_code_message.no_error), 200
    except Exception as e:
        response['exception'] = e
        return make_response(data=response, status_code=generic_error_code_message.generic_error), 500
