from selenium import webdriver
import math
import os

url = 'http://suninjuly.github.io/file_input.html'

browser = webdriver.Chrome()
browser.get(url)

element = browser.find_element_by_tag_name('[placeholder="Enter first name"]')
element.send_keys('FirstName')

element = browser.find_element_by_tag_name('[placeholder="Enter last name"]')
element.send_keys('LastName')

element = browser.find_element_by_tag_name('[placeholder="Enter email"]')
element.send_keys('Email')

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
element = browser.find_element_by_tag_name('[type="file"]')
element.send_keys(file_path)

button = browser.find_element_by_css_selector('button.btn')
button.click()


browser.quit()