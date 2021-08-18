from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    input_field = browser.find_element_by_css_selector(".form-control")
    input_field.send_keys(y)

    radiobutton = browser.find_element_by_css_selector("[id='robotCheckbox']")
    radiobutton.click()

    browser.execute_script("window.scrollBy(0, 100);")

    checkbox = browser.find_element_by_css_selector("[id='robotsRule']")
    checkbox.click()

    submit_button = browser.find_element_by_css_selector("button.btn")
    submit_button.click()






finally:
    time.sleep(10)
    browser.quit()

