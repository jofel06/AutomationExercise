from Locators.Page_Locators import AddToCart
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
import logging
import datetime

# this create a logger instance
logger = logging.getLogger(__name__)

def test_add_to_cart(driver, take_screenshot, request):
    browser_name = driver.capabilities.get('browserName', 'unknown')
    test_file_name = request.node.parent.name  # This gives the test file's name

    logger.info(f'{browser_name} browser opened successfully')
    driver.get('https://automationexercise.com/')
    add_to_cart_without_account = AddToCart(driver)

    try:
        logger.info(f'Page Title: {driver.title}') # Log the title of the page
        products_link = add_to_cart_without_account.Productslink()
        products_link.button_click()
        driver.execute_script('window.scrollBy(0, 300)')

        # Assert that the product page is opened (check for a unique element)
        try:
            WebDriverWait(driver, 10).until(EC.title_is("Automation Exercise - All Products"))
            logger.info('Redirected to Products page')
        except Exception:
            raise AssertionError("Test Failed: Products page not opened")

        """Add to Cart the first product"""
        logger.info('Viewing Product 1')
        ChooseProduct1 = add_to_cart_without_account.Product1()
        ChooseProduct1.hover_over()
        Product1_AddToCart = add_to_cart_without_account.Product1_AddToCart()
        Product1_AddToCart.button_click()

        # Assert that the 'Continue Shopping' button appears after adding the product to the cart
        ContinueShopping_button = add_to_cart_without_account.ContinueShoppingButton()
        assert ContinueShopping_button.is_displayed(), "Test Failed: Continue Shopping button not displayed"
        ContinueShopping_button.button_click()
        logger.info("Product 1 added to cart")

        """View the 2nd product and change the Quantity"""
        logger.info('Clicking product 2')
        add_to_cart_without_account.ViewProduct_2().button_click()
        logger.info('Changing quantity to 2')
        ChangeQuantity = add_to_cart_without_account.ChangeQuantity()
        ChangeQuantity.hover_over()
        driver.execute_script("arguments[0].stepUp();",
                               ChangeQuantity.web_element)  # Use JavaScript to change the quantity (step up to increase is, down to decrease)

        # Assert that the quantity was updated
        updated_quantity = ChangeQuantity.get_attribute('value')
        new_quantity = int(updated_quantity)
        if new_quantity == 2:
            logger.info('Product Quantity changed correctly')
        else:
            raise AssertionError("Test Failed: Quantity not updated")

        """Write Review"""
        logger.info("Writing a review")
        add_to_cart_without_account.EnterName().input_text('My name')
        add_to_cart_without_account.EnterEmail().input_text('sample@gmail.com')
        add_to_cart_without_account.AddReview().input_text('This is my Review\n'
                                   'This is the 2nd line of Review\n'
                                   '3rd line of Review')
        driver.execute_script('window.scrollBy(0, 800)')
        SubmitReview = add_to_cart_without_account.SubmitReview()
        SubmitReview.button_click()

        # Assert that the review was submitted (check for success message)
        assert "Thank you for your review." in driver.page_source, "Test Failed: Review not submitted"

        """Add to Cart and view cart"""
        logger.info('Adding product 2 to cart')
        AddToCartButton = add_to_cart_without_account.Product2_add_to_cart()
        AddToCartButton.button_click()
        logger.info('Viewing cart page')
        ViewCartLink = add_to_cart_without_account.ViewCart()
        ViewCartLink.button_click()
        # Assert that the cart page is opened
        try:
            WebDriverWait(driver, 10).until(EC.title_is("Automation Exercise - Checkout"))
            logger.info('Redirected to Cart page')
        except Exception:
            raise AssertionError("Test Failed: Cart page not opened")

        """Delete an item from the cart and then checkout"""
        logger.info("Deleting an item")
        DeleteFromCart_button = add_to_cart_without_account.DeleteItemfromCart()
        DeleteFromCart_button.button_click()

        """Proceed to Checkout"""
        logger.info("Proceeding to Checkout")
        ProceedToCheckout_button = add_to_cart_without_account.ProceedToCheckout()
        ProceedToCheckout_button.button_click()

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        screenshot_error = (f"Error_Screenshot_at_{test_file_name}_using_{browser_name}_on_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png")
        take_screenshot(screenshot_error)
        pytest.fail(f"test failed due to: {e}")
