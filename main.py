from services.factory_services import *
from singleton.checker_app_version_manager import checker_app_version_service
from helper.debug_message import *
from flask_apscheduler import APScheduler
from init_server import *
class ConfigScheduler:
    JOBS = [
        {
            "id": "periodic_job",
            "func": "jobs:periodic_job",
            "trigger": "interval",
            "minutes": 1,
        }
    ]
    SCHEDULER_API_ENABLED = True
def create_app(config_app=ConfigScheduler()):
    app = init_services()
    app.config.from_object(ConfigScheduler())
    if not init_server():
        show_message_debug("Error", TypeMessage.ERROR)
        exit(-1)
    scheduler = APScheduler()
    checker_app_version_service.check_apps_version()
    scheduler.init_app(app)
    scheduler.start()
    return app

flask_app = create_app()

if __name__ == '__main__':
    show_message_debug("main")
    checker_app_version_service.check_apps_version()
    flask_app.run(host="0.0.0.0", port=6000)
