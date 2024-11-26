import pytest
from Locators.Page_Locators import UserRegistration
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import logging
import datetime

from conftest import take_screenshot

logger = logging.getLogger(__name__)

def test_user_registration(driver, take_screenshot):
    browser_name = driver.capabilities.get('browserName', 'unknown')
    logger.info(f'{browser_name} browser opened successfully')

    driver.get('https://automationexercise.com/')
    user_registration = UserRegistration(driver)

    try:
        logger.info('Browser opened successfully')
        signup_login = user_registration.signup_login_icon()
        signup_login.button_click()

        try:
            WebDriverWait(driver, 10).until(EC.title_is("Automation Exercise - Signup / Login"))
            logger.info('Redirected to Signup / login page')
        except Exception:
            raise AssertionError("Test Failed: Signup / Registration page not opened")

        logger.info('Typing New username and email address')
        user_registration.new_user_name().input_text('myusername01011')
        user_registration.new_user_email().input_text('123sample01011@gmail.com')

        logger.info('Clicking Signup button')
        signup = user_registration.button_signup()
        signup.button_click()
        try:
            WebDriverWait(driver, 10).until(EC.title_is("Automation Exercise - Signup"))
            logger.info('Redirected to Signup / Registration page')
        except Exception:
            raise AssertionError("Test Failed: Signup / Registration page not opened")

        logger.info('Typing Account Information')
        choose_title = user_registration.choose_title()
        choose_title.button_click()
        user_registration.enter_password().input_text('samplepassword')
        user_registration.select_day().dropdown_select('1')
        user_registration.select_month().dropdown_select('December')
        user_registration.select_year().dropdown_select('2003')

        logger.info('Checking sign up News letter and Receive Special offers checkbox')
        signup_newsletter = user_registration.choose_newsletter_signup()
        signup_newsletter.button_click()
        receive_special_offers = user_registration.choose_receive_special_offers()
        receive_special_offers.button_click()

        logger.info('Typing Address Information')
        user_registration.enter_firstname().input_text('John')
        user_registration.enter_lastname().input_text('DaGreat')
        user_registration.enter_company().input_text('Sample Company')
        user_registration.enter_address1().input_text('This is address 1')
        user_registration.enter_address2().input_text('This is address 2')
        user_registration.select_country().dropdown_select('Canada')
        user_registration.enter_state().input_text('State of Canada')
        user_registration.enter_city().input_text('City of Canada')
        user_registration.enter_zip().input_text('0001')
        user_registration.enter_mobile_number().input_text('09123456789')

        logger.info('Clicking the Create Account button')
        create_account = user_registration.button_create_account()
        create_account.button_click()

        try:
            WebDriverWait(driver, 10).until(EC.title_is("Automation Exercise - Account Created"))
            logger.info('Account Registration Successful')
        except Exception:
            raise AssertionError("Test Failed: Account Registration Failed")

        user_registration.cont_account().button_click()
        user_registration.delete_acct().button_click()
        logger.info('Account Successfully Deleted')

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        screenshot_error = (f"Error_Screenshot_at_{browser_name}_on_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png")
        take_screenshot(screenshot_error)
        pytest.fail()

