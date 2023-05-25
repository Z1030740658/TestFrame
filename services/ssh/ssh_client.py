from configs import SSH_USER, SSH_HOST, SSH_PASSWORD, SSH_PORT
import paramiko
from utils.logger import log


class BaseSSHClient:
    """
    Base class for SSH clients.
    Shall be used as a context manager to ensure that connections are opened/closed when needed
    """

    def __init__(self, host=SSH_HOST, port=SSH_PORT, user=SSH_USER, password=SSH_PASSWORD):
        """Initialize SSH connections"""
        self.host = host
        self.port= int(port)
        self.user = user
        self.password = password
        ssh_config = {"hostname": self.host, "username": self.user, "password": self.password, "port": self.port,
                      "allow_agent": False, "look_for_keys": False}
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(**ssh_config)

    def execute_one(self, cmd):
        stdin, stdout, stderr = self.client.exec_command(cmd, timeout=100)
        res = stdout.read().decode('utf-8')
        err = stderr.read().decode('utf-8')
        log.info(res + err)
        return res + err

    def execute_all(self, cmd):
        result = ''
        for single_cmd in cmd.split(';'):
            stdin, stdout, stderr = self.client.exec_command(cmd, timeout=100)
            res = stdout.read().decode('utf-8')
            err = stderr.read().decode('utf-8')
            log.info(res + err)
            result = result + res + err
        return result

    def close(self):
        """
        Close SSH connections
        """
        self.client.close()
