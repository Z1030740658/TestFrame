import os
import pytest
from appium import webdriver
from configs import PLATFORM_NAME, PLATFORM_VERSION, DEVICE_NAME
from configs import APPIUM_URL
from configs import APK
from utils import PROJECT_PATH
from utils.logger import log


@pytest.fixture()
def appium_driver():
    """
    Get webdriver
    :return: driver instance object
    """
    driver = get_driver()

    yield driver
    # close the browser
    driver.quit()


def get_driver():
    """
    Set the following env vars:

    CAPABILITIES

    :return: driver
    """
    desired_caps = {}
    # desired_caps.update(CAPABILITIES) #in case you have the whole object of capabilities somewhere read from config
    desired_caps["platformName"] = PLATFORM_NAME
    desired_caps["platformVersion"] = PLATFORM_VERSION
    desired_caps["deviceName"] = DEVICE_NAME
    desired_caps["app"] = os.path.join(PROJECT_PATH, APK)
    log.info(f"Appium is listening: {APPIUM_URL}")
    log.info(f"Desired capabilities are: {desired_caps}")
    driver = webdriver.Remote(
        command_executor=APPIUM_URL,
        desired_capabilities=desired_caps,
        keep_alive=True)
    return driver
