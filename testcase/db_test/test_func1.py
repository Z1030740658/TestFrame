from services.db.db_client import BaseDbClient
from utils.logger import log


class TestDemon:
    def setup(self):
        self.db_client = BaseDbClient(database='mysql')

    def test_func1(self):
        execute_sql = 'select * from t1;'
        res = self.db_client.query_one(execute_sql)
        log.info(res)

    def teardown(self):
        self.db_client.close()
# pipenv run pytest tests/web_ui
# pipenv run pytest tests/web_ui/test_search_for_driver_docs.py
