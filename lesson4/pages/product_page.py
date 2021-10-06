from pages.base_page import BasePage
# from .base_page import BasePage - for linux and PyCharm
from pages.locators import MainPageLocators
from pages.locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        product_link = self.browser.find_element(*MainPageLocators.ADD_TO_BASKET_LINK)
        product_link.click()
        self.solve_quiz_and_get_code()
        
    def should_be_right_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME)
        assert product_name.text == added_product_name.text, "The name of added product is wrong"    

    def should_be_right_cost(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        added_product_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE)
        assert product_price.text == added_product_price.text, "The cost of added product is wrong"