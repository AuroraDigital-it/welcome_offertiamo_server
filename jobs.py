from singleton.checker_app_version_manager import checker_app_version_service
from helper.debug_message import *

def periodic_job():
    checker_app_version_service.check_apps_version()
