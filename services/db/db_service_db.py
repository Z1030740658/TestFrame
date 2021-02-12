from configs import DB_HOST, DB_USER, DB_PASSWORD
from services.db.db_client import BaseDbClient
from utils.logger import log


class DbServiceDbClient(BaseDbClient):
    """Db service DB client"""

    def __init__(self):
        super().__init__(DB_HOST, DB_USER, DB_PASSWORD, "database")

    def cleanup_all_users_data(self, user_id):
        """Remove data from db service DB"""
        users_tables = [("groups", "user_id"),
                        ("roles", "user_id")]

        for table, column in users_tables:
            query = f"delete from {table} where {column} = {user_id}"
            self.cursor.execute(query)
            log.debug("Removed %d rows from '%s' table", self.cursor.rowcount, table)

        # Remove user from users table
        self.cursor.execute(f"delete from users where user_id = {user_id}")
        log.debug("Removed %d rows from 'users' table", self.cursor.rowcount)

        self.connection.commit()
