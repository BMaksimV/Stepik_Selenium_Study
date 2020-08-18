from selenium import webdriver
import math



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


url = 'http://suninjuly.github.io/redirect_accept.html'

browser = webdriver.Chrome()
browser.get(url)

button = browser.find_element_by_css_selector('button.trollface.btn')
button.click()

new_tab = browser.window_handles[1]
browser.switch_to.window(new_tab)


# confirm = browser.switch_to.alert
# confirm.accept()

x = browser.find_element_by_css_selector('#input_value').text
x = calc(x)

answer = browser.find_element_by_css_selector('#answer')
answer.send_keys(x)

button = browser.find_element_by_css_selector('button.btn')
button.click()


browser.quit()
