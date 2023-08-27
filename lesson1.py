from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
url = "https://suninjuly.github.io/selects1.html"
browser.get(url)
browser.maximize_window()


def summa(a, b):
    return str(int(a) + int(b))


value_a = browser.find_element(By.ID, "num1").text
value_b = browser.find_element(By.ID, "num2").text
x = summa(value_a, value_b)

result = Select(browser.find_element(By.ID, "dropdown"))
result.select_by_value(str(x))

submit = browser.find_element(By.CSS_SELECTOR, "button, input")
submit.click()

time.sleep(15)
browser.quit()
