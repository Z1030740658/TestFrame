from appium_pages.base_screen import BaseScreen


class NextScreen(BaseScreen):
    def __init__(self, driver):
        super().__init__(driver)

    def allow_permissions(self):
        allow_1 = self.wait.until_elements_presence_by_id('permission_allow_button')
        if allow_1 is not False:
            allow_1[0].click()

        allow_2 = self.wait.until_elements_presence_by_id('permission_allow_button')
        if allow_2 is not False:
            allow_2[0].click()

    @property
    def title(self):
        title = self.wait.until_element_visible_by_id('title')
        return title.text
