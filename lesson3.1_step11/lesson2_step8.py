from selenium import webdriver
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element_by_css_selector("[name='firstname']")
    firstname.send_keys('Имя')

    lastname = browser.find_element_by_css_selector("[name='lastname']")
    lastname.send_keys('Фамилия')    

    email = browser.find_element_by_css_selector("[name='email']")
    email.send_keys('email')


    file_button = browser.find_element_by_css_selector("#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    file_button.send_keys(file_path)

    submit_button = browser.find_element_by_css_selector("button.btn")
    submit_button.click()




finally:
    time.sleep(10)
    browser.quit()