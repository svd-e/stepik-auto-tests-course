from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_button = browser.find_element_by_css_selector("button.btn")
    first_button.click()

    browser.switch_to.window(browser.window_handles[1])


    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(y)

    submit_button = browser.find_element_by_css_selector("button.btn")
    submit_button.click()



finally:
    time.sleep(10)
    browser.quit()