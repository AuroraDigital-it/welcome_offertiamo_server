from singleton.redis_manager import redis_manager
from singleton.checker_app_version_manager import checker_app_version_service
import helper.debug_message as debug_message
import config


def init_server() -> bool:
    debug_message.show_message_debug("START CHECK INIT SERVER!", debug_message.TypeMessage.INFO)
    # # Check if redis is available
    if not redis_manager.is_redis_available():
        debug_message.show_message_debug("REDIS NOT CONNECTED! " + config.REDIS_DATABASE_HOST,
                                         debug_message.TypeMessage.ERROR)
    else:
        debug_message.show_message_debug("REDIS CONNECTED! " + config.REDIS_DATABASE_HOST,
                                         debug_message.TypeMessage.INFO)
    # Get last version of apps
    debug_message.show_message_debug("START INIT VERSIONS!", debug_message.TypeMessage.INFO)
    checker_app_version_service.check_apps_version()
    debug_message.show_message_debug("END INIT VERSIONS!", debug_message.TypeMessage.INFO)
    debug_message.show_message_debug("FINISH CHECK INIT SERVER!", debug_message.TypeMessage.SUCCESS)
    return True
