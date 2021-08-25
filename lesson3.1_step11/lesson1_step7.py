from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("[id='treasure']")
    x = x_element.get_attribute("valuex")
    y = calc(float(x))

    input_field = browser.find_element_by_css_selector("[id='answer']")
    input_field.send_keys(y)

    radiobutton = browser.find_element_by_css_selector("[id='robotCheckbox']")
    radiobutton.click()

    radiobutton = browser.find_element_by_css_selector("[id='robotsRule']")
    radiobutton.click()

    submit_button = browser.find_element_by_css_selector("button.btn")
    submit_button.click()






finally:
    time.sleep(10)
    browser.quit()

