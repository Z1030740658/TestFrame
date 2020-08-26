from appium_pages.base_screen import BaseScreen
from appium_pages.next_screen import NextScreen


class LoginScreen(BaseScreen):
    def __init__(self, driver):
        super().__init__(driver)

    def login_to_app(self, username, password):
        """
        Login to the account
        with provided username and password
        :param username: str
        :param password: str
        :return:
        """
        username_input = self.wait.until_element_visible_by_id('usernameInput')
        username_input.send_keys(username)

        pass_input = self.wait.until_element_visible_by_id('passwordInput')
        pass_input.send_keys(password)

        signin_button = self.wait.until_element_visible_by_id('signInButton')
        signin_button.click()

        return NextScreen(self.driver)
