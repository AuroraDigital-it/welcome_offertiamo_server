from flask import Blueprint
from helper.response_helper import make_response
import constant.exception.generic_error_code_message as generic_error_code_message
from singleton.checker_app_version_manager import checker_app_version_service

base_api = Blueprint('base_api_v1', __name__, url_prefix='/api/v1/welcome/')


@base_api.route("/init")
def init():
    response = dict()

    response['android_version'] = checker_app_version_service.version_app_android \
        if checker_app_version_service.version_app_android else ""

    response['ios_version'] = checker_app_version_service.version_app_ios \
        if checker_app_version_service.version_app_ios else ""

    return make_response(data=response, status_code=generic_error_code_message.no_error), 200


@base_api.route("/info")
def init():
    response = dict()
    response['last_update'] = checker_app_version_service.last_check
    response['android_version'] = checker_app_version_service.version_app_android \
        if checker_app_version_service.version_app_android else ""

    response['ios_version'] = checker_app_version_service.version_app_ios \
        if checker_app_version_service.version_app_ios else ""
    return make_response(data=response, status_code=generic_error_code_message.no_error), 200
    