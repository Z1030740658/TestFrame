import pytest

from utils.logger import log

pytest_plugins = [
    "fixtures.api_setup",
    "fixtures.appium_setup",
    "fixtures.webdriver_setup"
]


def get_test_meta(item):
    """
    Retrieve test ID and summary from the test
    """
    test_id = item.name.replace("test_", "")
    item_doc = item.obj.__doc__
    test_summary = item_doc.strip() if item_doc else None
    return test_id, test_summary


def pytest_runtest_setup(item):
    test_id, _ = get_test_meta(item)
    log.info("Setup for test: '%s'", test_id)


def pytest_runtest_call(item):
    test_id, test_summary = get_test_meta(item)
    log.info("Start test: '%s'", test_id)
    if test_summary:
        log.info("Test summary: '%s'", test_summary)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    result = outcome.get_result()

    test_id, _ = get_test_meta(item)

    if result.when == 'call':
        if result.failed:
            log.info("Test '%s' finished: FAILED", test_id)
        elif result.passed:
            log.info("Test '%s' finished: PASSED", test_id)

    elif result.failed:
        log.info("Test result of '%s': FAILED on '%s'", test_id, result.when)


def pytest_addoption(parser):
    """
    Makes possible to pass employee through command line by --driver key.
    """
    parser.addoption("--driver", action="store")  
