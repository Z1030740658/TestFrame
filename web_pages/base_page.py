import time
from web_pages.waits import Waits
from utils.logger import log
from selenium.webdriver.common.by import By
from fixtures.webdriver_setup import get_browser_driver


class BasePage:
    """
    BasePage should contain all common site-page functionality
    """

    def __init__(self, driver=get_browser_driver()):
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

    def find_by_xpath(self, xpath):
        """find element by xpath"""
        self.driver.find_element(by=By.XPATH, value=xpath)