import pytest
import logging
import os
from datetime import datetime
from selenium import webdriver
from config import BASE_URL

#This is the "MAIN ENTRY POINT"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# Create Reports directory if it doesn't exist
REPORTS_DIR = os.path.join(os.getcwd(), 'Reports')
SCREENSHOTS_DIR = os.path.join(REPORTS_DIR, 'screenshots')

os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

@pytest.fixture(scope='function')
def driver(request):
    logging.info("Launching browser")

    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    driver.maximize_window()

    # Store driver in request for failure access
    request.driver = driver

    yield driver

    logging.info("Closing browser")
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture screenshot on test failure"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        if hasattr(item, 'funcargs') and 'driver' in item.funcargs:
            driver = item.funcargs['driver']
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"{item.name}_{timestamp}.png"
            screenshot_path = os.path.join(SCREENSHOTS_DIR, screenshot_name)

            try:
                driver.save_screenshot(screenshot_path)
                logger.info(f"Screenshot saved: {screenshot_path}")
            except Exception as e:
                logger.error(f"Failed to capture screenshot: {str(e)}")
