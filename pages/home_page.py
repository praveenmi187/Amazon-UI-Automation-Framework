from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.login_page import LoginPage
from base.base_page import BasePage

class HomePage(BasePage):
    ACCOUNT_LIST = (By.ID,'nav-link-accountList')
    sign_in = (By.XPATH,'//span[text()="Sign in"]')

    def hover_on_account_list(self):
        account_list = self.wait_for_visibility(self.ACCOUNT_LIST)
        ActionChains(self.driver).move_to_element(account_list).perform()

    def click_sign_in(self):
        self.hover_on_account_list()
        self.safe_click(self.sign_in)
        return LoginPage(self.driver)
