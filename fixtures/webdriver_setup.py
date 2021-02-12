import pytest
import os
from selenium.webdriver import DesiredCapabilities, Chrome, Firefox, Safari
from selenium.webdriver.chrome.options import Options as ch_options
from selenium.webdriver.firefox.options import Options as ff_options
from configs import WEB_DRIVER, HEADLESS
from utils.logger import log
from utils import PROJECT_PATH


@pytest.fixture()
def web_driver():
    driver = get_browser_driver()
    driver.set_window_size(1920, 1080)  # set default screen size

    yield driver
    # close the browser
    driver.quit()


def get_browser_driver():
    """
    Using following env vars:
    WEB_DRIVER: name of the driver "chrome", "firefox"

    Get web-driver - choose between Chrome, Firefox etc.
    :return: driver instance object
    """
    capabilities = dict(getattr(DesiredCapabilities, WEB_DRIVER))
    log.info(f"Webdriver is: {WEB_DRIVER}, running headless: {HEADLESS}")
    if WEB_DRIVER == 'CHROME':
        chromedriver = os.path.join(PROJECT_PATH, "chromedriver.exe")
        chrome_options = ch_options()
        if HEADLESS:
            chrome_options.set_headless()
        browser_driver = Chrome(executable_path=chromedriver,
                                desired_capabilities=capabilities,
                                options=chrome_options)
    elif WEB_DRIVER == 'FIREFOX':
        geckodriver = os.path.join(PROJECT_PATH, "geckodriver.exe")
        firefox_options = ff_options()
        if HEADLESS:
            firefox_options.set_headless()
        browser_driver = Firefox(executable_path=geckodriver,
                                 capabilities=capabilities,
                                 options=firefox_options)
    elif WEB_DRIVER == 'SAFARI':
        safaridriver = os.path.join(PROJECT_PATH, "safaridriver.exe")
        # headless mode is not possible right now in Safari
        browser_driver = Safari(executable_path=safaridriver,
                                capabilities=capabilities)
    else:
        raise Exception('Unknown/unsupported driver selected: ' + WEB_DRIVER)

    return browser_driver
