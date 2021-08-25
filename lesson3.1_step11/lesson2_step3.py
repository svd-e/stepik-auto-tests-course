from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


try: 
    link = "http://suninjuly.github.io/selects1.html"
    # link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#num1")
    x = int(x_element.text)
    print(x)

    y_element = browser.find_element_by_css_selector("#num2")
    y = int(y_element.text)

    z = str(x + y)
    
    select = Select(browser.find_element_by_css_selector(".custom-select"))
    select.select_by_value(z)
    
    submit_button = browser.find_element_by_css_selector("button.btn")
    submit_button.click()


finally:
    time.sleep(10)
    browser.quit()

