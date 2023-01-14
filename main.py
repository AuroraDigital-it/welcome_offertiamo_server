import config
import helper.debug_message as dbg_message
import init_server as init
from services.factory_services import *
from singleton.checker_app_version_manager import checker_app_version_service
import traceback
import schedule
import threading
import time

flask_app = init_services()


def periodic_job():
    schedule.every(10).minutes.do(checker_app_version_service.check_apps_version)
    while True:
        schedule.run_pending()
        time.sleep(1)


try:
    if not init.init_server():
        print("###### THERE WAS AN ERROR, CHECK THE LOGS ######")
        exit(-1)

    dbg_message.show_message_debug(message="START DAEMONS",
                                   type_message=dbg_message.TypeMessage.INFO)
    # Start daemon
    daemon = threading.Thread(target=periodic_job, daemon=True, name="PeriodicChecker")
    daemon.start()

except Exception as e:
    dbg_message.show_message_debug(message="EXCEPTION CAPTURED IN MAIN",
                                   type_message=dbg_message.TypeMessage.ERROR)
    traceback.print_exc()

if __name__ == '__main__':
    flask_app.run(host="0.0.0.0")
