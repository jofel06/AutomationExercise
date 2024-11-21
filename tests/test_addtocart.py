from selenium import webdriver
from Locators.Page_Locators import AddToCart
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import logging
import datetime
import pytest
# this create a logger instance
logger = logging.getLogger(__name__)

@pytest.fixture
def browser():
    logger.info('Launching Google Chrome Browser')
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    logger.info("Test completed, closing browser")
    browser.quit()

def test_add_to_cart(browser):
    browser.get('https://automationexercise.com/')
    add_to_cart = AddToCart(browser)

    try:
        logger.info('Browser opened successfully')
        products_link = add_to_cart.Productslink()
        products_link.button_click()
        browser.execute_script('window.scrollBy(0, 300)')

        # Assert that the product page is opened (check for a unique element)
        try:
            WebDriverWait(browser, 10).until(EC.title_is("Automation Exercise - All Products"))
            logger.info('Redirected to Products page')
        except Exception:
            raise AssertionError("Test Failed: Products page not opened")

        """Add to Cart the first product"""
        logger.info('Viewing Product 1')
        ChooseProduct1 = add_to_cart.Product1()
        ChooseProduct1.hover_over()
        Product1_AddToCart = add_to_cart.Product1_AddToCart()
        Product1_AddToCart.button_click()

        # Assert that the 'Continue Shopping' button appears after adding the product to the cart
        ContinueShopping_button = add_to_cart.ContinueShoppingButton()
        assert ContinueShopping_button.is_displayed(), "Test Failed: Continue Shopping button not displayed"
        ContinueShopping_button.button_click()
        logger.info("Product 1 added to cart")

        """View the 2nd product and change the Quantity"""
        logger.info('Clicking product 2')
        add_to_cart.ViewProduct_2().button_click()
        logger.info('Changing quantity to 2')
        ChangeQuantity = add_to_cart.ChangeQuantity()
        ChangeQuantity.hover_over()
        browser.execute_script("arguments[0].stepUp();",
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
        add_to_cart.EnterName().input_text('My name')
        add_to_cart.EnterEmail().input_text('sample@gmail.com')
        add_to_cart.AddReview().input_text('This is my Review\n'
                                   'This is the 2nd line of Review\n'
                                   '3rd line of Review')
        browser.execute_script('window.scrollBy(0, 800)')
        SubmitReview = add_to_cart.SubmitReview()
        SubmitReview.button_click()

        # Assert that the review was submitted (check for success message)
        assert "Thank you for your review." in browser.page_source, "Test Failed: Review not submitted"

        """Add to Cart and view cart"""
        logger.info('Adding product 2 to cart')
        AddToCartButton = add_to_cart.AddtoCartButton()
        AddToCartButton.button_click()
        logger.info('Viewing cart page')
        ViewCartLink = add_to_cart.ViewCart()
        ViewCartLink.button_click()
        # Assert that the cart page is opened
        try:
            WebDriverWait(browser, 10).until(EC.title_is("Automation Exercise - Checkout"))
            logger.info('Redirected to Cart page')
        except Exception:
            raise AssertionError("Test Failed: Cart page not opened")

        """Delete an item from the cart and then checkout"""
        logger.info("Deleting an item")
        DeleteFromCart_button = add_to_cart.DeleteItemfromCart()
        DeleteFromCart_button.button_click()

        """Proceed to Checkout"""
        logger.info("Proceeding to Checkout")
        ProceedToCheckout_button = add_to_cart.ProceedToCheckout()
        ProceedToCheckout_button.button_click()

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        # Take a screenshot when an error occurs
        add_to_cart.take_screenshot(f"error_screenshot_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png")
        pytest.fail(f"Test Failed: {e}")
