from appium_pages.login_screen import LoginScreen
from configs import APP_USERNAME, APP_PASSWORD


def test_log_in_go_next(appium_driver):
    login_page = LoginScreen(appium_driver)
    next_screen = login_page.login_to_app(APP_USERNAME, APP_PASSWORD)
    next_screen.allow_permissions()
    assert next_screen.title == 'Title'

# pipenv run pytest tests/android_ui
# pipenv run pytest tests/android_ui/test_go_forward.py
