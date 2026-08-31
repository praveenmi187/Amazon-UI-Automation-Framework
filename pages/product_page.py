import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from pages.cart_page import CartPage

#module level logger
logger = logging.getLogger(__name__)

class ProductPage(BasePage):

    PRODUCT_LINKS = (By.XPATH, "//div[@data-component-type='s-search-result']//a[@class ='a-link-normal s-no-outline']")
    ADD_TO_CART = (By.ID, "add-to-cart-button")
    ADD_TO_YOUR_ORDER = (By.XPATH,"//input[@aria-labelledby='attachSiNoCoverage-announce'] | //button[contains(@aria-label,'No Thanks')]")
    GO_TO_CART = (By.XPATH, "//a[contains(@href,'cart')]")

    def select_product(self):
        logger.info(f"Current URL: {self.driver.current_url}")

        def action():
            products = self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCT_LINKS))
            logger.info(f"Products found:{len(products)}")

            for i in range (len(products)):
                try:
                    #RE-FETCH ELEMENT EVERYTIME
                    products = self.driver.find_elements(*self.PRODUCT_LINKS)
                    product = products[i]


                    if product.is_displayed():
                        self.scroll_to_element(product)

                        #fresh element inside retry
                        self.retry(lambda: self.driver.find_elements(*self.PRODUCT_LINKS)[i].click())
                        logger.info("Product clicked")
                        return

                except Exception as e:
                    logger.info(f"Skipped due to: {str(e)}")
                    continue

            raise Exception("No clickable product found")
        return self.retry(action)

    # ---------- Function: Add to Cart ----------
    def add_to_cart(self):

        logger.info(f"Current URL: {self.driver.current_url}")

        try:
            add_button = self.wait.until(
                EC.element_to_be_clickable(self.ADD_TO_CART)
            )

            self.scroll_to_element(add_button)

            self.retry(lambda: self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART)).click())

            logger.info("Product added to cart")

        except Exception as e:
            logger.error(f"Add to Cart failed: {str(e)}")
            raise
        return CartPage(self.driver)

    #------------ADD TO YOUR ORDER------------------
    def add_to_your_order(self):

        logger.info("Handling 'Add to your order' popup if present...")

        try:

            buttons = self.driver.find_elements(*self.ADD_TO_YOUR_ORDER)

            if buttons:
                logger.info("Popup detected")

                btn = buttons[0]

                self.scroll_to_element(btn)

                self.retry(lambda: self.driver.find_elements(*self.ADD_TO_YOUR_ORDER)[0].click())
                logger.info("Clicked 'No Thanks / Skip'")

            else:
                logger.info("No popup appeared")

        except Exception as e:
            logger.info(f"Popup handling skipped: {str(e)}")
        return CartPage(self.driver)

    # ---------- Function: Go to Cart ----------
    def go_to_cart(self):

        try:
            cart_btn = self.wait.until(
                EC.element_to_be_clickable(self.GO_TO_CART))

            self.retry(lambda: self.wait.until(EC.element_to_be_clickable(self.GO_TO_CART)).click())
            logger.info("Navigated to cart")

        except Exception as e:
            raise Exception (f"Cart navigation failed: {str(e)}")

        return CartPage(self.driver)
