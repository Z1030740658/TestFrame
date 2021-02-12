from services.db.db_client import BaseDbClient
from mysql.connector import Error
from utils.logger import log


class DBService(BaseDbClient):
    def __init__(self, host, user, password, database=None):
        super().__init__(host, user, password, database)

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
