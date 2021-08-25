import time
link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


# запускается pytest --language=es test_items.py

def test_guest_should_see_add_to_basket_btn(browser):
    browser.get(link)
    time.sleep(5)
    assert browser.find_element_by_css_selector(".btn-add-to-basket"), "There is no 'Add to basket' button on this page"
