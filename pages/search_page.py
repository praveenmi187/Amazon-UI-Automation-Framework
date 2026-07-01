from selenium.webdriver.common.by import By
from base.base_page import BasePage
from pages.product_page import ProductPage


class SearchPage(BasePage):
    SEARCH_BOX = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID,'nav-search-submit-button')

    def search_products(self,product_name):
        self.wait_for_visibility(self.SEARCH_BOX).send_keys(product_name)
        self.safe_click(self.SEARCH_BUTTON)
        return ProductPage(self.driver)
