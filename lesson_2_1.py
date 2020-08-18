import math

from selenium import webdriver
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



url = 'http://suninjuly.github.io/get_attribute.html'


browser = webdriver.Chrome()
browser.get(url)

element = browser.find_element_by_id('treasure')
x = element.get_attribute('valuex')

# x_element = browser.find_element_by_id('input_value')
# x = x_element.text
y = calc(x)

element = browser.find_element_by_id('answer')
element.send_keys(y)

element = browser.find_element_by_id('robotCheckbox')
element.click()

element = browser.find_element_by_id('robotsRule')
element.click()

element = browser.find_element_by_css_selector('button.btn')
element.click()


time.sleep(15)
browser.quit()