import json
import os
from utils import PROJECT_PATH


def get_env_config(env):
    """Get test environment config from file"""
    config_file_name = os.path.join(PROJECT_PATH, "configs", "envs", "development.json".format(env))
    with open(config_file_name, "r") as config_file:
        env_config = config_file.read()
    return json.loads(env_config)


def get_node_info(env):
    """Get test nodeinfo from file"""
    node_file_name = os.path.join(PROJECT_PATH, "configs", "envs", "node.json".format(env))
    with open(node_file_name, "r") as node_file:
        node_info = node_file.read()
    return json.loads(node_info)