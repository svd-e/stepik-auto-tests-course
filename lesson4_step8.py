from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

    book_button = browser.find_element_by_css_selector("button.btn")
    book_button.click()

    x_element = browser.find_element_by_css_selector('#input_value')
    y = calc(x_element.text)

    input_field = browser.find_element_by_css_selector(".form-control")
    input_field.send_keys(y)

    submit_button = browser.find_element_by_css_selector("#solve")
    submit_button.click()

finally:
    time.sleep(30)
    browser.quit()