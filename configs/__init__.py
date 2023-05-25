import os
from os import getenv
from utils.logger import log

from dotenv import load_dotenv

from configs.env_config import get_env_config
from utils import PROJECT_PATH

dotenv_file = os.path.join(PROJECT_PATH, ".env")
if os.path.exists(dotenv_file):
    load_dotenv(dotenv_file)

# Test environment configuration
ENV = getenv("ENV")
_env_config = get_env_config(ENV)

log.info(f"Environment is: {ENV}")

# API hosts
REST_SERVICE_HOST = _env_config["rest_service_host"]

# UI wait time
UI_MAX_RESPONSE_TIME = 25.0

# Android
APP_USERNAME = _env_config["app_username"]
APP_PASSWORD = _env_config["app_password"]

# Appium
APPIUM_URL = "http://127.0.0.1:4723/wd/hub"
PLATFORM_NAME = "Android"
PLATFORM_VERSION = "10.0"
DEVICE_NAME = "Pixel 2"
APK = "awesome.apk"

# Webdriver
WEB_URL = _env_config["web_host"]
WEB_DRIVER = "CHROME"
HEADLESS = False

# DB
DB_HOST = _env_config["db_connection"]["host"]
DB_USER = _env_config["db_connection"]["username"]
DB_PASSWORD = _env_config["db_connection"]["password"]
DB_TYPE = _env_config["db_connection"]["db_type"]
DB_PORT = _env_config["db_connection"]["db_port"]

#SSH
SSH_PORT = _env_config["ssh_connection"]["ssh_port"]
SSH_USER = _env_config["ssh_connection"]["ssh_username"]
SSH_HOST = _env_config["ssh_connection"]["ssh_host"]
SSH_PASSWORD = _env_config["ssh_connection"]["ssh_password"]
