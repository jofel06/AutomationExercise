import pytest
import logging
import datetime

from Locators.Page_Locators import AddToCart
from Locators.Page_Locators import ValidLogin
from tests.Valid_Login.conftest import valid_login_credentials
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

@pytest.mark.parametrize('valid_login_credentials', [("sampleuser01@yahoo.com", "thisispass01")])
def test_add_to_cart_with_valid_account(driver, valid_login_credentials, take_screenshot, request):
    browser_name = driver.capabilities.get('browserName', 'unknown')
    test_file_name = request.node.parent.name

    email, password = valid_login_credentials

    driver.get("https://automationexercise.com/")
    add_to_cart_with_valid_account = AddToCart(driver)
    valid_login_credentials = ValidLogin(driver)
    logger.info(f'{browser_name} browser opened successfully')

    try:
        assert "Automation Exercise" in driver.title, "Website not opened"
        valid_login_credentials.signup_login_icon().button_click()
        try:
            WebDriverWait(driver, 10).until(EC.title_is("Automation Exercise - Signup / Login"))
            logger.info("Signup / Login page opened")
        except Exception:
            raise AssertionError("Test failed: Signup / Registration page not opened")

        logger.info("Entering valid email")
        valid_login_credentials.enter_valid_email().input_text(email)
        logger.info("Entering valid password")
        valid_login_credentials.enter_valid_password().input_text(password)
        logger.info("Logging in")
        valid_login_credentials.valid_login_button().button_click()
        try:
            WebDriverWait(driver, 10).until(EC.title_is("Automation Exercise"))
            logger.info("Login Successful, redirected to the Homepage")
        except Exception:
            raise AssertionError("Test failed: Login failed")

        logger.info("Opening product page")
        add_to_cart_with_valid_account.Productslink().button_click()
        try:
            WebDriverWait(driver, 10).until(EC.title_is("Automation Exercise - All Products"))
            logger.info("Product page opened")
            driver.execute_script('window.scrollBy(0, 500)')
        except Exception:
            raise AssertionError("Test failed: Product page was not opened")

        """Adding Product 1 to cart"""
        logger.info("Selecting product 1")
        add_to_cart_with_valid_account.Product1().hover_over()
        logger.info("Adding to Cart")
        add_to_cart_with_valid_account.Product1_AddToCart().button_click()
        logger.info("Item successfully added to cart")

        ContinueShopping_button = add_to_cart_with_valid_account.ContinueShoppingButton()
        assert ContinueShopping_button.is_displayed(), "Test Failed: Continue Shopping button not displayed"
        ContinueShopping_button.button_click()
        logger.info("Continue browsing")

        """Adding Product 2 to cart"""
        logger.info("Viewing product 2")
        add_to_cart_with_valid_account.ViewProduct_2().button_click()
        logger.info("Changing quantity to 2")

        product_2_change_quantity = add_to_cart_with_valid_account.ChangeQuantity()
        product_2_change_quantity.hover_over()
        driver.execute_script("arguments[0].stepUp();",product_2_change_quantity.web_element)  # Use JavaScript to change the quantity (step up to increase is, down to decrease)

        # Assert that the quantity was updated
        updated_quantity = product_2_change_quantity.get_attribute('value')
        new_quantity = int(updated_quantity)
        if new_quantity == 2:
            logger.info('Product Quantity changed correctly')
        else:
            raise AssertionError("Test Failed: Quantity not updated")

        """Writing a Review"""
        logger.info("Writing a review")
        add_to_cart_with_valid_account.EnterName().input_text('My name')
        add_to_cart_with_valid_account.EnterEmail().input_text('sample@gmail.com')
        add_to_cart_with_valid_account.AddReview().input_text('This is my Review\n'
                                   'This is the 2nd line of Review\n'
                                   '3rd line of Review')
        driver.execute_script('window.scrollBy(0, 800)')

        add_to_cart_with_valid_account.SubmitReview().button_click()
        assert "Thank you for your review." in driver.page_source, "Test Failed: Review not submitted"

        """Adding product 2 to cart and viewing the cart"""
        logger.info('Adding product 2 to cart')
        add_to_cart_with_valid_account.Product2_add_to_cart().button_click()
        logger.info('Opening the cart page')
        add_to_cart_with_valid_account.ViewCart().button_click()
        try:
            WebDriverWait(driver, 10).until(EC.title_is("Automation Exercise - Checkout"))
            logger.info('Redirected to Cart page')
        except Exception:
            raise AssertionError("Test Failed: Cart page not opened")

        """Deleting an item from the cart and checking out"""
        logger.info("Deleting an item")
        add_to_cart_with_valid_account.DeleteItemfromCart().button_click()

        logger.info("Proceeding to Checkout")
        add_to_cart_with_valid_account.ProceedToCheckout().button_click()
        try:
            WebDriverWait(driver, 10).until(EC.title_is("Automation Exercise - Checkout"))
            logger.info("Successfully redirected to Checkout page")
        except Exception:
            raise AssertionError("Test Failed: Checkout page not opened")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        screenshot_error = (f"Error_Screenshot_at_{test_file_name}_using_{browser_name}_on_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png")
        take_screenshot(screenshot_error)
        pytest.fail(f"test failed due to: {e}")




