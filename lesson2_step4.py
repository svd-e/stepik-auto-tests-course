from selenium import webdriver
import time

try:
	browser = webdriver.Chrome()
	browser.execute_script("document.title='Кысь-кысь';alert('Мя!');")

finally:
    time.sleep(10)
    browser.quit()