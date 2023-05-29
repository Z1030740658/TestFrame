import time

from web_pages.base_page import BasePage
from configs import WEB_URL
from utils.enums.urls import Urls


class TestDemon:
    def setup(self):
        self.basepage = BasePage()

    def test_func1(self):
        # self.basepage.driver.get(WEB_URL + Urls.test_url.value)
        self.basepage.driver.get(WEB_URL + Urls.test_url.value)
        time.sleep(3)
        self.basepage.wait_page_loaded()

    def teardown(self):
        self.basepage.driver.quit()
# pipenv run pytest tests/web_ui
# pipenv run pytest testcase/web_ui/test_func1.py
