from selenium import webdriver

import math
import os


# element.send_keys(file_path)


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

x = browser.find_element_by_id('input_value').text
func = calc(x)

edit = browser.find_element_by_id('answer')
edit.send_keys(func)

button = browser.find_element_by_css_selector("button.btn")
browser.execute_script('return arguments[0].scrollIntoView(true);', button)

element = browser.find_element_by_id('robotCheckbox')
element.click()

element = browser.find_element_by_id('robotsRule')
element.click()





button.click()



browser.quit()