import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.dashboard_page import DashboardPage
from base.base_page import BasePage

logger = logging.getLogger(__name__)


class LoginPage(BasePage):
    EMAIL = (By.ID, 'ap_email_login')
    CONTINUE = (By.XPATH, '//input[@type = "submit"]')
    PASSWORD = (By.ID, "ap_password")
    SIGN_IN = (By.ID, 'signInSubmit')

    ERROR_MESSAGE = (By.ID, 'auth-error-message-box')
    CAPTCHA = (By.ID, 'auth-captcha-image')
    SUCCESS_HEADER = (By.ID,"nav-link-accountList-nav-line-1")

    def __init__(self,driver):
        super().__init__(driver)
        self.page_validation(self.EMAIL)

    #wait until any result appears (SUCCESS,ERROR, CAPTCHA)
    def wait_for_login_result(self):
        print('Before waiting, current URL:',self.driver.current_url)

        try:
            self.wait.until(
                EC.any_of(
                    EC.presence_of_element_located(self.SUCCESS_HEADER),
                    EC.visibility_of_element_located(self.ERROR_MESSAGE),
                    EC.visibility_of_element_located(self.CAPTCHA)
                )
            )
        except Exception:
            print('Timeout at URL:', self.driver.current_url)
            raise


    #CHECK ERROR
    def is_error_displayed(self):
        elements = self.driver.find_elements(*self.ERROR_MESSAGE)
        return len(elements) > 0

    #CHECK CAPTCHA
    def is_captcha_displayed(self):
        elements = self.driver.find_elements(*self.CAPTCHA)
        return len(elements) > 0

    #GET ERROR TEXT SAFELY
    def get_error_message_text(self):
        if self.is_error_displayed():
            return self.wait_for_visibility(self.ERROR_MESSAGE).text
        return None

    #LOGIN METHOD (returns page based on result)
    def login(self,email, password):
        logger.info("logging in....")

        #we use wait_for_visibility from our basepage
        self.wait_for_visibility(self.EMAIL).send_keys(email)
        self.safe_click(self.CONTINUE)

        self.wait_for_visibility(self.PASSWORD).send_keys(password)
        self.safe_click(self.SIGN_IN)

        #wait for state change after login/signin click
        self.wait_for_login_result()

        #CAPTCHA HANDLING
        if self.is_captcha_displayed():
            raise Exception ('Captcha detected. Cannot automate login.')

        #If ERROR -> stay on LoginPage
        if self.is_error_displayed():
            return self
        #If success -> Go to DashboardPage
        else:
            return DashboardPage(self.driver)