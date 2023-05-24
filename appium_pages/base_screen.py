from appium_pages.waits import Waits
from utils.logger import log
from fixtures.appium_setup import get_driver

class BaseScreen:
    """
    BasePage should contain all common site-page functionality
    """

    def __init__(self, driver=get_driver()):
        self.driver = driver

    @property
    def wait(self):
        """
        Init class Waits(selenium waits).
        (e.g: self.wait.until....)
        :return:
        """
        return Waits(self.driver)
