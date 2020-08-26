import json
import os
from utils import PROJECT_PATH


def get_env_config(env):
    """Get test environment config from file"""
    config_file_name = os.path.join(PROJECT_PATH, "configs", "envs", "{}.json".format(env))
    with open(config_file_name, "r") as config_file:
        env_config = config_file.read()
    return json.loads(env_config)
