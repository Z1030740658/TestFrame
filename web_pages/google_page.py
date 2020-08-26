from web_pages.base_page import BasePage
from configs import WEB_URL
from utils.enums.test_urls import TestUrls
from web_pages.search_result_page import SearchResultPage
from selenium.webdriver.common.keys import Keys


class GooglePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def search(self, question):
        self.driver.get(WEB_URL + TestUrls.test_url.value)
        search_input = self.wait.until_element_visible_by_name('q')
        search_input.send_keys(question)
        search_input.send_keys(Keys.ENTER)
        
        return SearchResultPage(self.driver)
