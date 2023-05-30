import os
from os import getenv

from dotenv import load_dotenv

from configs.env_config import get_env_config
from configs.env_config import get_node_info
from utils import PROJECT_PATH
from utils.logger import log

dotenv_file = os.path.join(PROJECT_PATH, ".env")
if os.path.exists(dotenv_file):
    load_dotenv(dotenv_file)

# Test environment configuration
ENV = getenv("ENV")
_env_config = get_env_config(ENV)
_node_info = get_node_info(ENV)

log.info(f'Environment is: {_env_config["env_name"]}')

# API hosts
REST_SERVICE_HOST = _env_config["rest_service_host"]

# UI wait time
UI_MAX_RESPONSE_TIME = 25.0

# Android
APP_USERNAME = _env_config["app_username"]
APP_PASSWORD = _env_config["app_password"]

# Appium
APPIUM_URL = _env_config["appium_url"]
PLATFORM_NAME = _env_config["platform_name"]
PLATFORM_VERSION = _env_config["platform_version"]
DEVICE_NAME = _env_config["device_name"]
APK = _env_config["apk"]

# Webdriver
WEB_URL = _env_config["web_host"]
WEB_DRIVER = _env_config["web_driver"]
HEADLESS = False

# PRI_DB
PRI_DB_HOST = _node_info["pri_db"]["host"]
PRI_DB_USER = _node_info["pri_db"]["username"]
PRI_DB_PASSWORD = _node_info["pri_db"]["password"]
PRI_DB_TYPE = _node_info["pri_db"]["db_type"]
PRI_DB_PORT = _node_info["pri_db"]["db_port"]

# S1_DB
S1_DB_HOST = _node_info["sta1_db"]["host"]
S1_DB_USER = _node_info["sta1_db"]["username"]
S1_DB_PASSWORD = _node_info["sta1_db"]["password"]
S1_DB_TYPE = _node_info["sta1_db"]["db_type"]
S1_DB_PORT = _node_info["sta1_db"]["db_port"]

# S2_DB
S2_DB_HOST = _node_info["sta2_db"]["host"]
S2_DB_USER = _node_info["sta2_db"]["username"]
S2_DB_PASSWORD = _node_info["sta2_db"]["password"]
S2_DB_TYPE = _node_info["sta2_db"]["db_type"]
S2_DB_PORT = _node_info["sta2_db"]["db_port"]


# PRI_SSH
PRI_SSH_HOST = _node_info["pri_ssh"]["ssh_host"]
PRI_SSH_USER = _node_info["pri_ssh"]["ssh_username"]
PRI_SSH_PASSWORD = _node_info["pri_ssh"]["ssh_password"]
PRI_SSH_PORT = _node_info["pri_ssh"]["ssh_port"]

# S1_SSH
S1_SSH_HOST = _node_info["sta1_ssh"]["ssh_host"]
S1_SSH_USER = _node_info["sta1_ssh"]["ssh_username"]
S1_SSH_PASSWORD = _node_info["sta1_ssh"]["ssh_password"]
S1_SSH_PORT = _node_info["sta1_ssh"]["ssh_port"]

# S2_SSH
S2_SSH_HOST = _node_info["sta2_ssh"]["ssh_host"]
S2_SSH_USER = _node_info["sta2_ssh"]["ssh_username"]
S2_SSH_PASSWORD = _node_info["sta2_ssh"]["ssh_password"]
S2_SSH_PORT = _node_info["sta2_ssh"]["ssh_port"]
