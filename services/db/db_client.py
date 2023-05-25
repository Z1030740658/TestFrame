from configs import DB_HOST, DB_USER, DB_PASSWORD, DB_TYPE, DB_PORT
import mysql.connector


class BaseDbClient:
    """
    Base class for DB clients.
    Shall be used as a context manager to ensure that connections are opened/closed when needed.
    Usage (applies for all child classes):
    with DataBaseClient as db_client:  # connections are being opened this line
        db_client.some_method()
    # after we exit 'with' block, connections are closed.
    """

    def __init__(self, database, host=DB_HOST, PORT=DB_PORT, user=DB_USER, password=DB_PASSWORD, dbtype=DB_TYPE):
        """Initialize DB connections"""
        self.host = host
        self.port= int(port)
        self.dbtype = dbtype
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None
        db_config = {"host": self.host, "user": self.user, "password": self.password, "port": self.port}
        if self.database:
            db_config["database"] = self.database
        self.connection = mysql.connector.connect(**db_config)
        self.cursor = self.connection.cursor(buffered=True)

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
