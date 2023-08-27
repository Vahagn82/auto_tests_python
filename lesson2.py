from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math

browser = webdriver.Chrome()
url = "http://suninjuly.github.io/execute_script.html"
browser.get(url)
browser.maximize_window()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


value_x = browser.find_element(By.XPATH, "//*[@id='input_value']").text
y = calc(value_x)


browser.execute_script("window.scrollBy(0, 100);")
input = browser.find_element(By.XPATH, "//*[@id='answer']")
input.send_keys(str(y))

check = browser.find_element(By.XPATH, "//*[@id='robotCheckbox']")
check.click()

radio = browser.find_element(By.XPATH, "//*[@id='robotsRule']")
radio.click()

submit = browser.find_element(By.CSS_SELECTOR, "button, select")
submit.click()

time.sleep(15)
browser.quit()




