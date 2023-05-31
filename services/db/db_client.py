import mysql.connector
from mysql.connector import Error
import psycopg2
import cx_Oracle

import configs
from utils.logger import log


class BaseDbClient:
    """
    Base class for DB clients.
    Shall be used as a context manager to ensure that connections are opened/closed when needed.
    Usage (applies for all child classes):
    with DataBaseClient as db_client:  # connections are being opened this line
        db_client.some_method()
    # after we exit 'with' block, connections are closed.
    """

    def __init__(self, database, node='pri', host=configs.PRI_DB_HOST, port=configs.PRI_DB_PORT,
                 user=configs.PRI_DB_USER, password=configs.PRI_DB_PASSWORD, dbtype=configs.PRI_DB_TYPE):
        """Initialize DB connections"""
        if node == 'sta1':
            self.host = configs.S1_DB_HOST
            self.port = int(configs.S1_DB_HOST)
            self.dbtype = configs.S1_DB_TYPE
            self.user = configs.S1_DB_USER
            self.password = configs.S1_DB_PASSWORD
        elif node == 'sta2':
            self.host = configs.S2_DB_HOST
            self.port = int(configs.S2_DB_HOST)
            self.dbtype = configs.S2_DB_TYPE
            self.user = configs.S2_DB_USER
            self.password = configs.S2_DB_PASSWORD
        else:
            self.host = host
            self.port = int(port)
            self.dbtype = dbtype
            self.user = user
            self.password = password
        self.database = database
        self.connection = None
        self.cursor = None
        db_config = {"host": self.host, "user": self.user, "password": self.password,
                     "port": self.port, "database": self.database}
        try:
            if self.dbtype == 'mysql':
                self.connection = mysql.connector.connect(**db_config)
                self.cursor = self.connection.cursor(buffered=True)
            elif self.dbtype == 'opengauss':
                self.connection = psycopg2.connect(**db_config)
                self.cursor = self.connection.cursor()
            elif self.dbtype == 'oracle':
                self.connection = cx_Oracle.connect(**db_config)
                self.cursor = self.connection.cursor()
        except Exception as e:
            log.info('------DB connected fail info start------')
            log.error(str(e))
            log.info('------DB connected fail info end------')

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
        Close DB connections at exit
        """
        self.cursor.close()
        self.connection.close()
