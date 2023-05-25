from services.ssh import BaseSSHClient

class TestDemon:
    def setup(self):
        self.ssh_client = BaseSSHClient()

def test_func1(self):
    cmd = 'uname -a'
    self.ssh_client.execute(cmd)

def teardown(self):
    self.basepage.driver.quit()
# pipenv run pytest tests/web_ui
# pipenv run pytest tests/web_ui/test_search_for_driver_docs.py
