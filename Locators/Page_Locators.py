from BaseElement.Base_Page import BaseElement
from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger(__name__)

class UserRegistration:
    def __init__(self, driver):
        self.driver = driver

    def signup_login_icon(self):
        locator = (By.XPATH, "//div[@class='shop-menu pull-right']//a[@href='/login']")
        return BaseElement(self.driver, locator)

    def new_user_name(self):
        locator = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
        return BaseElement(self.driver, locator)

    def new_user_email(self):
        locator = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
        return BaseElement(self.driver, locator)

    def button_signup(self):
        locator = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
        return BaseElement(self.driver, locator)

    def choose_title(self):
        locator = (By.ID, "id_gender1")
        return BaseElement(self.driver, locator)

    def enter_password(self):
        locator = (By.ID, "password")
        return BaseElement(self.driver, locator)

    def select_day(self):
        locator = (By.ID, "days")
        return BaseElement(self.driver, locator)

    def select_month(self):
        locator = (By.ID, "months")
        return BaseElement(self.driver, locator)

    def select_year(self):
        locator = (By.ID, "years")
        return BaseElement(self.driver, locator)

    def choose_receive_special_offers(self):
        locator = (By.ID, "optin")
        return BaseElement(self.driver, locator)

    def choose_newsletter_signup(self):
        locator = (By.ID, "newsletter")
        return BaseElement(self.driver, locator)

    def enter_firstname(self):
        locator = (By.ID, "first_name")
        return BaseElement(self.driver, locator)

    def enter_lastname(self):
        locator = (By.ID, "last_name")
        return BaseElement(self.driver, locator)

    def enter_company(self):
        locator = (By.ID, "company")
        return BaseElement(self.driver, locator)

    def enter_address1(self):
        locator = (By.ID, "address1")
        return BaseElement(self.driver, locator)

    def enter_address2(self):
        locator = (By.ID, "address2")
        return BaseElement(self.driver, locator)

    def select_country(self):
        locator = (By.ID, "country")
        return BaseElement(self.driver, locator)

    def enter_state(self):
        locator = (By.ID, "state")
        return BaseElement(self.driver, locator)

    def enter_city(self):
        locator = (By.ID, "city")
        return BaseElement(self.driver, locator)

    def enter_zip(self):
        locator = (By.ID, "zipcode")
        return BaseElement(self.driver, locator)

    def enter_mobile_number(self):
        locator = (By.ID, "mobile_number")
        return BaseElement(self.driver, locator)

    def button_create_account(self):
        locator = (By.CSS_SELECTOR, "button[data-qa='create-account']")
        return BaseElement(self.driver, locator)

    def cont_account(self):
        locator = (By.XPATH, "//div[@class='pull-right']//a[@class='btn btn-primary']")
        return BaseElement(self.driver, locator)

    def delete_acct(self):
        locator = (By.XPATH, "//ul[@class='nav navbar-nav']//i[@class='fa fa-trash-o']")
        return BaseElement(self.driver, locator)


class AddToCart:
    def __init__(self, driver):
        self.driver = driver

    def Productslink(self):
        locator = (By.XPATH,"//div[@class='shop-menu pull-right']//a[@href='/products']")
        return BaseElement(self.driver, locator)

    def Product1(self):
        locator = (By.XPATH, "//div[@class='col-sm-4']//img[@src='/get_product_picture/1']")
        return BaseElement(self.driver, locator)

    def Product1_AddToCart(self):
        locator = (By.XPATH, "//div[@class='overlay-content']//a[@data-product-id='1']")
        return BaseElement(self.driver, locator)

    def ContinueShoppingButton(self):
        locator = (By.CSS_SELECTOR, "button[class='btn btn-success close-modal btn-block']")
        return BaseElement(self.driver, locator)

    def ViewProduct_2(self):
        locator = (By.XPATH, "//div[@class='product-image-wrapper']//a[@ href='/product_details/2']")
        return BaseElement(self.driver, locator)

    def ChangeQuantity(self):
        locator = (By.CSS_SELECTOR, "input[id='quantity']")
        return BaseElement(self.driver, locator)

    def AddtoCart(self):
        locator = (By.CSS_SELECTOR, "button[class='btn btn-default cart']")
        return BaseElement(self.driver, locator)

    def AddtoCartButton(self):
        locator = (By.CSS_SELECTOR, "button[class='btn btn-default cart']")
        return BaseElement(self.driver, locator)

    def EnterName(self):
        locator = (By.ID, "name")
        return BaseElement(self.driver, locator)

    def EnterEmail(self):
        locator = (By.ID, "email")
        return BaseElement(self.driver, locator)

    def AddReview(self):
        locator = (By.ID, "review")
        return BaseElement(self.driver, locator)

    def SubmitReview(self):
        locator = (By.ID, "button-review")
        return BaseElement(self.driver, locator)

    def ViewCart(self):
        locator = (By.XPATH, "//div[@class='modal-content']//a")
        return BaseElement(self.driver, locator)

    def DeleteItemfromCart(self):
        locator = (By.XPATH, "//td[@class='cart_delete']//a[@data-product-id='2']")
        return BaseElement(self.driver, locator)

    def ProceedToCheckout(self):
        locator = (By.CSS_SELECTOR, "a[class='btn btn-default check_out']")
        return BaseElement(self.driver, locator)

class ValidLogin:
    def __init__(self, driver):
        self.driver = driver

    def signup_login_icon(self):
        locator = (By.XPATH, "//div[@class='shop-menu pull-right']//a[@href='/login']")
        return BaseElement(self.driver, locator)

    def enter_valid_email(self):
        locator = (By.CSS_SELECTOR, "input[data-qa='login-email']")
        return BaseElement(self.driver, locator)

    def enter_valid_password(self):
        locator = (By.CSS_SELECTOR, "input[data-qa='login-password']")
        return BaseElement(self.driver, locator)

    def valid_login_button(self):
        locator = (By.CSS_SELECTOR, "button[data-qa='login-button']")
        return BaseElement(self.driver, locator)

    def logout_button(self):
        locator = (By.XPATH, "//div[@class='shop-menu pull-right']//a[@href='/logout']")
        return BaseElement(self.driver, locator)






