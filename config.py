import os
from dotenv import load_dotenv

load_dotenv(".env")
# LOADS ENVIRONMENTS FILE (.env) IF EXISTS ELSE USE DEFAULTS VALUE
REDIS_DATABASE_HOST = os.getenv('REDIS_DATABASE_HOST', '127.0.0.1')
REDIS_DATABASE_PORT = os.getenv('REDIS_DATABASE_PORT', 6379)
REDIS_DATABASE_USERNAME = os.getenv('REDIS_DATABASE_USERNAME', None)
REDIS_DATABASE_PASSWORD = os.getenv('REDIS_DATABASE_PASSWORD', None)
ID_APP_IOS = os.getenv('ID_APP_IOS','com.auroradigital.offertiamo')
ID_APP_ANDROID = os.getenv('ID_APP_ANDROID', 'com.auroradigital.offertiamo')
COUNTRY_STORE_ANDROID = os.getenv('COUNTRY_STORE_ANDROID', 'it')
LANG_STORE_ANDROID = os.getenv('LANG_STORE_ANDROID', 'it')
DEBUG = os.getenv('DEBUG', True)
