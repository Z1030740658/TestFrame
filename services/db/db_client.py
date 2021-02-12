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

    def __init__(self, host, user, password, database):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None

    def __enter__(self):
        """Initialize DB connections"""
        db_config = {"host": self.host, "user": self.user, "password": self.password}
        if self.database:
            db_config["database"] = self.database

        self.connection = mysql.connector.connect(**db_config)
        self.cursor = self.connection.cursor(buffered=True)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close DB connections at exit
        """
        self.cursor.close()
        self.connection.close()
