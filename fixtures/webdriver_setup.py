import pytest
from selenium.webdriver import Chrome, DesiredCapabilities, Firefox
from selenium.webdriver.chrome.options import Options
from configs import WEB_DRIVER, HEADLESS
from utils.logger import log


@pytest.fixture()
def web_driver():
    """
    Set the following env vars:

    TST_DRIVER: name of the driver "chrome", "firefox"
    TST_SELENIUM: url to the Selenium Grid Hub

    :return: driver
    """
    # choose between Remote or local or Headless Chrome, Firefox
    driver = get_browser_driver()
    driver.set_window_size(1920, 1080)  # set default screen size

    yield driver
    # close the browser
    driver.quit()


def get_browser_driver():
    """
    Get web-driver
    :return: driver instance object
    """
    capabilities = dict(getattr(DesiredCapabilities, WEB_DRIVER))
    log.info(f"Webdriver is: {WEB_DRIVER}, running headless: {HEADLESS}")
    if WEB_DRIVER == 'CHROME':
        chrome_options = Options()
        if HEADLESS:
            chrome_options.set_headless()
        browser_driver = Chrome(
            desired_capabilities=capabilities, options=chrome_options)

    elif WEB_DRIVER == 'FIREFOX':
        browser_driver = Firefox(capabilities=capabilities)
    else:
        raise Exception('Unknown/unsupported driver selected: ' + WEB_DRIVER)

    return browser_driver
