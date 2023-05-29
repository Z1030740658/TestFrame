from services.ssh.ssh_client import BaseSSHClient


class TestDemon:
    def setup(self):
        self.ssh_client = BaseSSHClient()

    def test_func1(self):
        cmd = 'uname -a'
        self.ssh_client.execute_one(cmd)

    def teardown(self):
        self.ssh_client.close()
# pipenv run pytest tests/web_ui
# pipenv run pytest tests/web_ui/test_search_for_driver_docs.py
