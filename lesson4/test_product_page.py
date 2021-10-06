from pages.product_page import ProductPage
# from pages.main_page import MainPage
import time

def test_guest_can_add_product_to_basket(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_right_name()
    page.should_be_right_cost()
    # time.sleep(5)

# pytest -v -s --tb=line --language=en test_product_page.py
# "lesson 4.3 step 2. Adding product to cart ver. 0"