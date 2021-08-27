from pages.main_page import MainPage
# from .pages.main_page import MainPage  - for linux and PyCharm


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина


# pytest -v --tb=line --language=en test_main_page.py
# lesson 4.1 step 6. preparation ver. 0