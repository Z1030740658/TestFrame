from web_pages.google_page import GooglePage


def test_search_for_driver_docs(web_driver):
    google_page = GooglePage(web_driver)
    result_page = google_page.search('webdriver documentation for selenium')
    assert result_page.get_first_result_link() == 'https://www.selenium.dev/documentation/en/webdriver/'

# pipenv run pytest tests/web_ui
# pipenv run pytest tests/web_ui/test_search_for_driver_docs.py
