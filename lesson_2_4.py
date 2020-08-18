from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

url = 'http://suninjuly.github.io/explicit_wait2.html'

browser = webdriver.Chrome()
browser.get(url)

price = WebDriverWait(browser, 13).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
)

button = browser.find_element_by_css_selector('button#book')
button.click()


x = browser.find_element_by_css_selector('#input_value').text
x = calc(x)

answer = browser.find_element_by_css_selector('#answer')
answer.send_keys(x)

button = browser.find_element_by_css_selector('button#solve')
button.click()

time.sleep(10)
browser.quit()
