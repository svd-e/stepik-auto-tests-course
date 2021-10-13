from pages.base_page import BasePage
# from .base_page import BasePage - for linux and PyCharm
# from pages.locators import BasePageLocators
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    # def should_be_basket_page(self):
    #     self.should_be_basket_url()
    #     self.should_be_basket()


    # def should_be_basket_url(self):
    #     # проверка на корректный url адрес
    #     assert "basket" in self.url

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_NOT_EMPTY_LINK), "Basket is not empty"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "There is no empty basket text"


