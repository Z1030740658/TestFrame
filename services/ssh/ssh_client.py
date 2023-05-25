from configs import SSH_USER, SSH_HOST, SSH_PASSWORD, SSH_PORT
import paramiko


class BaseSshClient:
    """
    Base class for SSH clients.
    Shall be used as a context manager to ensure that connections are opened/closed when needed
    """

    def __init__(self, host=SSH_HOST, port=SSH_HOST, user=SSH_USER, password=SSH_PASSWORD):
        """Initialize SSH connections"""
        self.host = host
        self.port= int(port)
        self.user = user
        self.password = password
        ssh_config = {"hostname": self.host, "username": self.user, "password": self.password, "port": self.port}
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.connection = self.client.connect(**ssh_config)

    def execute(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except Error as e:
            log.error(f"Error on query execution: {e}")
            raise e

    def query_all(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as e:
            log.error(f"Error on query execution: {e}")
            raise e

    def query_one(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchone()
        except Error as e:
            log.error(f"Error on query execution: {e}")
            raise e

    def close(self):
        """
        Close SSH connections at exit
        """
        self.cursor.close()
        self.connection.close()
