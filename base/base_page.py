import time
import logging
import pytest

from selenium.common import StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#------------------------------------logging setup-------------------------------
logger = logging.getLogger(__name__)

#---------------------------------------Base page---------------------------------
class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,15)

#-----------------wait for visibility-----------------------------------

    def wait_for_visibility(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

#------------------------wait for clickable-----------------------------

    def wait_for_clickable(self,locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

 #----------------------scroll to element--------------------------------------

    def scroll_to_element(self,locator):
        return self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", locator)

#------------------------------Retry-----------------------------------------------------

    def retry(self, action, attempts = 3, delay =1):

        #store last error, if all retries fail
        last_exception = None

        for i in range(attempts):
            try:
                return action()
            except (StaleElementReferenceException, ElementClickInterceptedException) as e:
                last_exception = e
                logger.warning(f"Retry {i+1}: {str(e)}")
                time.sleep(delay)
        raise last_exception

#-------------------------safe click----------------------------------------------

    def safe_click(self,locator):
        try:
            #step1: wait
            element = self.wait_for_clickable(locator)

            #step2: scroll
            self.scroll_to_element(element)

            #step3: Retry normal click
            self.retry(lambda: element.click())
        except Exception as e:
            logger.warning("Normal click failed -> Trying JS Click:", str(e))

            #step 4: JS Click (last option)
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].click();", element)

#-----------------------------page validation-------------------------------------------
    def page_validation(self,locator):
        self.wait_for_visibility(locator)
