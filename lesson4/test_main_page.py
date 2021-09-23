from pages.main_page import MainPage
# from .pages.main_page import MainPage  - for linux and PyCharm
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    # login_page.should_be_login_page() # Для перехода между страницами. один из вариантов. Выбран другой
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

# def test_guest_should_see_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/accounts/login/"
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_login_page()




# pytest -v --tb=line --language=en test_main_page.py
# "lesson 4.2 step 8. LoginPage realization ver. 0"