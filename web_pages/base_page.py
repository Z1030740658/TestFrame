import time
from web_pages.waits import Waits
from utils.logger import log
from selenium.webdriver.common.by import By
from fixtures.webdriver_setup import get_browser_driver
from selenium.webdriver.common.keys import Keys


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

    def find_ele_xpath(self, value):
        """find element by xpath"""
        return self.driver.find_element(by=By.XPATH, value=value)

    def find_ele_id(self, value):
        """find element by id"""
        return self.driver.find_element(by=By.ID, value=value)

    def find_ele_name(self, value):
        """find element by name"""
        return self.driver.find_element(by=By.NAME, value=value)

    def find_ele_classname(self, value):
        """find element by classname"""
        return self.driver.find_element(by=By.CLASS_NAME, value=value)

    def find_ele_css(self, value):
        """find element by css"""
        return self.driver.find_element(by=By.CSS_SELECTOR, value=value)

    def find_eles_xpath(self, value):
        """find elements by xpath"""
        return self.driver.find_element(by=By.XPATH, value=value)

    def find_eles_id(self, value):
        """find elements by id"""
        return self.driver.find_element(by=By.ID, value=value)

    def find_eles_name(self, value):
        """find elements by name"""
        return self.driver.find_element(by=By.NAME, value=value)

    def find_eles_classname(self, value):
        """find elements by classname"""
        return self.driver.find_element(by=By.CLASS_NAME, value=value)

    def find_eles_css(self, value):
        """find elements by css"""
        return self.driver.find_element(by=By.CSS_SELECTOR, value=value)
