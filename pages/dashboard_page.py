from selenium.webdriver.common.by import By
from base.base_page import BasePage
from pages.search_page import SearchPage


class DashboardPage(BasePage):
#Locator for 'Hello, [Name]' text on the Amazon header
    WELCOME_TEXT = (By.ID,'nav-link-accountList-nav-line-1')

    def __init__(self,driver):
        super().__init__(driver)
#Ensures the dashboard has loaded by validating the welcome text exists
        self.page_validation(self.WELCOME_TEXT)

#Retrives the text from the welcome element (e.g.,'Hello,Victor')
    def get_logged_in_username(self):
        return self.wait_for_visibility(self.WELCOME_TEXT).text

    def go_to_search(self):
        return SearchPage(self.driver)


