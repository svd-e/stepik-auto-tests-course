from .base_page import BasePage
from .locators import MainPageLocators
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        product_link = self.browser.find_element(*MainPageLocators.ADD_TO_BASKET_LINK)
        product_link.click()
        # self.solve_quiz_and_get_code() Это нужно было для одного из заданий

    def should_be_right_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME)
        assert product_name.text == added_product_name.text, "The name of added product is wrong"

    def should_be_right_cost(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        added_product_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE)
        assert product_price.text == added_product_price.text, "The cost of added product is wrong"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message has not disappeared"
