import pytest
import logging
from selenium import webdriver
from config import BASE_URL

#This is the "MAIN ENTRY POINT"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@pytest.fixture(scope='function')
def driver():
    logging.info("Launching browser")

    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    driver.maximize_window()

    yield driver

    logging.info("Closing browser")
    driver.quit()
