import logging
import pytest
import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.Page_Locators import ValidLogin

logger = logging.getLogger(__name__)

def test_valid_login(driver, take_screenshot, valid_login_credentials):
    browser_name = driver.capabilities.get('browserName', 'unknown')
    logger.info(f'{browser_name} browser opened successfully')

    driver.get("https://automationexercise.com/")
    valid_login = ValidLogin(driver)

    email, password = valid_login_credentials #assign the email and password to the fixture

    try:
        assert "Automation Exercise" in driver.title, "Test Failed: Website was not opened"
        valid_login.signup_login_icon().button_click()
        try:
            WebDriverWait(driver, 10).until(EC.title_is("Automation Exercise - Signup / Login"))
            logger.info("Redirected to the Signup/Login page")
        except Exception:
            raise AssertionError("Test failed: Signup / Registration page not opened")

        logger.info("Entering valid email")
        valid_login.enter_valid_email().input_text(email)
        logger.info("Entering valid password")
        valid_login.enter_valid_password().input_text(password)

        valid_login.valid_login_button().button_click()
        try:
            WebDriverWait(driver, 10).until(EC.title_is("Automation Exercise"))
            logger.info("Login Successful, redirected to the Homepage")
        except Exception:
            raise AssertionError("Test failed: Login failed")

        logger.info("Logging out")
        valid_login.logout_button().button_click()

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        screenshot_error = (f"Error_Screenshot_at_{browser_name}_on_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png")
        take_screenshot(screenshot_error)
        pytest.fail()
