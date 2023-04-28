from enum import Enum
from itunes_app_scraper.scraper import AppStoreScraper, AppStoreException
from constant.database_constants import *
from google_play_scraper import app
import config
from datetime import datetime
from singleton.redis_manager import redis_manager

class PlatformType(Enum):
    IOS = 1
    ANDROID = 2


class CheckerAppVersion:
    def __init__(self):
        self.id_app_ios = config.ID_APP_IOS
        self.id_app_android = config.ID_APP_ANDROID

    def check_apps_version(self):
        scraper = AppStoreScraper()
        # Check iOS
        try:
            result = scraper.get_app_details(self.id_app_ios, country="it", lang="it", force=True)
            if result and result['version']:
                if result['version'] != "1.4.8":
                    redis_manager.redis_db.set(apple_version_key, result['version'])
            else:
                redis_manager.redis_db.set(apple_version_key, "")
        except AppStoreException:
            redis_manager.redis_db.set(apple_version_key, "")
        
        # Check Android
        try:
            result = app(
                self.id_app_android,
                lang=config.COUNTRY_STORE_ANDROID,
                country=config.LANG_STORE_ANDROID
            )
            if result and result['version']:
                 redis_manager.redis_db.set(android_version_key, result['version'])
            else:
                 redis_manager.redis_db.set(android_version_key, "")
        except Exception:
            redis_manager.redis_db.set(android_version_key, "")

        # Last update
        last_update = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        redis_manager.redis_db.set(last_update_version_key,last_update)


checker_app_version_service = CheckerAppVersion()
