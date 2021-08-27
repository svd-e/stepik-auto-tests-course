import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# pytest -v --tb=line --language=en test_main_page.py
# lesson 4.1 step 6. preparation ver. 0

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: ru, en, fr, etc.")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    
    yield browser
    print("\nquit browser..")
    browser.quit()