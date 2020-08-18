from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time

url = 'http://suninjuly.github.io/selects1.html'

browser = webdriver.Chrome()
browser.get(url)

num1 = browser.find_element_by_id('num1').text
num2 = browser.find_element_by_id('num2').text
# print(type(num1))

summa = int(num1) + int(num2)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(summa))

button = browser.find_element_by_css_selector('button.btn')
button.click()

# time.sleep(10)
browser.quit()
