import configs
import paramiko
from utils.logger import log


class BaseSSHClient:
    """
    Base class for SSH clients.
    Shall be used as a context manager to ensure that connections are opened/closed when needed
    """

    def __init__(self, node='pri', host=configs.PRI_SSH_HOST, port=configs.PRI_SSH_PORT,
                 user=configs.PRI_SSH_USER, password=configs.PRI_SSH_PASSWORD):
        """Initialize SSH connections"""
        if node == 'sta1':
            self.host = configs.S1_SSH_HOST
            self.port = int(configs.S1_SSH_PORT)
            self.user = configs.S1_SSH_USER
            self.password = configs.S1_SSH_PASSWORD
        elif node == 'sta2':
            self.host = configs.S2_SSH_HOST
            self.port = int(configs.S2_SSH_PORT)
            self.user = configs.S2_SSH_USER
            self.password = configs.S2_SSH_PASSWORD
        else:
            self.host = host
            self.port = int(port)
            self.user = user
            self.password = password
        ssh_config = {"hostname": self.host, "username": self.user, "password": self.password, "port": self.port,
                      "allow_agent": False, "look_for_keys": False}
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(**ssh_config)
        except Exception as e:
            log.info('------SSH connect failed info start------')
            log.error(str(e))
            log.info('------SSH connect failed info end------')

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
