from web_pages.base_page import BasePage


class SearchResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_first_result_link(self):
        first_result = self.wait.until_element_visible_by_xpath('//div[@class = "g"][1]/div/div[1]/a')
        return first_result.get_attribute('href')
