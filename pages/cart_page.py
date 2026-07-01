from base.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    CHECKOUT = (By.XPATH, "//input[@name ='proceedToRetailCheckout']")

    def proceed_to_checkout(self):
        self.safe_click(self.CHECKOUT)
        return