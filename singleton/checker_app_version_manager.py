from enum import Enum
from packaging import version
from itunes_app_scraper.scraper import AppStoreScraper, AppStoreException
from google_play_scraper import app
import config


class PlatformType(Enum):
    IOS = 1
    ANDROID = 2


class CheckerAppVersion:
    def __init__(self):
        self.id_app_ios = config.ID_APP_IOS
        self.id_app_android = config.ID_APP_ANDROID
        self.version_app_android = None
        self.version_app_ios = None
        
    def check_apps_version(self):
        scraper = AppStoreScraper()
        # Check iOS
        if self.id_app_ios:
            try:
                result = scraper.get_app_details(self.id_app_ios, country="it", lang="it")
                if result['version']:
                    self.version_app_ios = result['version']
                else: 
                    self.version_app_ios = None
            except AppStoreException:
                self.version_app_ios = None
        
        # Check Android
        if self.id_app_android:
            try: 
                result = app(
                    self.id_app_android,
                    lang=config.COUNTRY_STORE_ANDROID,
                    country=config.LANG_STORE_ANDROID
                )
                if result and result['version']: 
                    self.version_app_android = result['version']
                else:
                    self.version_app_android = None

            except Exception: 
                self.version_app_android = None

    def is_newest_android_version(self, app_version: str):
        last_version = self.version_app_android
        if not last_version:
            return True
        return version.parse(app_version) > version.parse(last_version)

    def is_newest_ios_version(self, app_version: str):
        last_version = self.version_app_ios
        if not last_version:
            return True
        return version.parse(app_version) > version.parse(last_version)


checker_app_version_service = CheckerAppVersion()
