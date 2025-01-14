import logging
import datetime
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.Page_Locators import ValidLogin

logger = logging.getLogger(__name__)

@pytest.mark.parametrize('valid_login_credentials', [("sampleuser01@yahoo.com", "thisispass01")]) #this will specifically use only the specified credential
def test_successful_login_with_valid_email_and_password(driver, valid_login_credentials, take_screenshot, request):

    browser_name = driver.capabilities.get('browserName', 'unknown') #for Logging
    test_file_name = request.node.parent.name #for Logging

    logger.info(f'{browser_name} browser opened successfully')
    driver.get("https://automationexercise.com/")
    valid_user_and_email = ValidLogin(driver)

    email, password = valid_login_credentials

    try:
        assert "Automation Exercise" in driver.title, "Test Failed, Website was not opened"
        valid_user_and_email.signup_login_icon().button_click()
        try:
            WebDriverWait(driver, 10).until(EC.title_is("Automation Exercise - Signup / Login"))
            logger.info("Redirected to the Signup/Login page")
        except Exception:
            raise AssertionError("Test failed: Signup / Registration page not opened")

        logger.info("Entering valid Email")
        valid_user_and_email.enter_valid_email().input_text(email)
        logger.info("Entering valid password")
        valid_user_and_email.enter_valid_password().input_text(password)

        logger.info("Logging in")
        valid_user_and_email.valid_login_button().button_click()
        try:
            WebDriverWait(driver, 10).until(EC.title_is("Automation Exercise"))
            logger.info("Login Successful, redirected to the Homepage")
        except Exception:
            raise AssertionError("Test failed: Login failed")

        logger.info("Logging out")
        valid_user_and_email.logout_button().button_click()

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        screenshot_error = (f"Error_Screenshot_at_{test_file_name}_using_{browser_name}_on_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png")
        take_screenshot(screenshot_error)


