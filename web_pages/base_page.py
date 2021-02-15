import time
from web_pages.waits import Waits
from utils.logger import log


class BasePage:
    """
    BasePage should contain all common site-page functionality
    """

    def __init__(self, driver):
        self.driver = driver

    @property
    def wait(self):
        """
        Init class Waits(selenium waits).
        (e.g: self.wait.until....)
        :return:
        """
        return Waits(self.driver)

    def wait_page_loaded(self):
        while True:
            time.sleep(1)
            if self.driver.execute_script('return document.readyState;') == 'complete':
                log.info("PAGE_LOADED")
                break
