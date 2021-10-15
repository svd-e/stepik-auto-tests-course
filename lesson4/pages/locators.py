from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ADD_TO_BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTRATION_PASSWORD_1 = (By.CSS_SELECTOR, "[name='registration-password1']")
    REGISTRATION_PASSWORD_2 = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTRATION_SUBMIT_BTN = (By.CSS_SELECTOR, "[name='registration_submit']")
    

class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_OPENING_LINK = (By.CSS_SELECTOR, ".btn-group .btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    # BASKET_OPENED_LINK = (By.CSS_SELECTOR, ".page-header")
    BASKET_IS_NOT_EMPTY_LINK = (By.CSS_SELECTOR, ".col-sm-6")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, ".content p")
    



# "lesson 4.3 step 14. Final result. ver. 0"