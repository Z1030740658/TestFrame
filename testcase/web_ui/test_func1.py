from web_pages.base_page import BasePage
from configs import WEB_URL
from utils.enums.urls import Urls

class TestDemon:
    def setup(self):
        self.basepage = BasePage()

def test_func1(self):
    self.basepage.driver.get(WEB_URL + Urls.test_url.value)
    self.basepage.wait_page_loaded()

def teardown(self):
    self.basepage.driver.quit()
# pipenv run pytest tests/web_ui
# pipenv run pytest tests/web_ui/test_search_for_driver_docs.py
