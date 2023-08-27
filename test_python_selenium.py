from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver_g = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver_g.get(base_url)
driver_g.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver_g.find_element(By.XPATH, "//*[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input login")
password = driver_g.find_element(By.XPATH, "//*[@id='password']")
password.send_keys(password_all)
print("Input password")
login_btn = driver_g.find_element(By.XPATH, "//*[@id='login-button']")
login_btn.click()
print("Click login button")

"""Info about Product #1"""
product_1 = driver_g.find_element(By.XPATH, "//*[@id='item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver_g.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = driver_g.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print("Add to cart")

cart = driver_g.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a/span")
cart.click()
print("Go to cart")

"""Info about product #1 in the cart"""
cart_product_1 = driver_g.find_element(By.XPATH, "//*[@id='item_4_title_link']")
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print("Info about product #1 is right")

price_cart_product_1 = driver_g.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_cart_product_1 = price_cart_product_1.text
print(value_price_cart_product_1)
assert value_price_product_1 == value_price_cart_product_1
print("Info about price is right")

checkout_btn = driver_g.find_element(By.XPATH, "//*[@id='checkout']")
checkout_btn.click()
print("You are ready for buy")

"""Input personal data"""
first_name = "Vahagn"
last_name = "Sargsyan"
postal_code = "2001"

user_first_name = driver_g.find_element(By.XPATH, "//*[@id='first-name']")
user_first_name.send_keys(first_name)
print("Enter User's first name")
user_last_name = driver_g.find_element(By.XPATH, "//*[@id='last-name']")
user_last_name.send_keys(last_name)
print("Enter User's last name")
user_postal_code = driver_g.find_element(By.XPATH, "//*[@id='postal-code']")
user_postal_code.send_keys(postal_code)
print("Enter User's postal code")
countinue_btn = driver_g.find_element(By.XPATH, "//*[@id='continue']")
countinue_btn.click()
print("Fine")

"""Info about product #1 in checkout"""
checkout_product_1 = driver_g.find_element(By.XPATH, "//*[@id='item_4_title_link']/div")
value_checkout_product_1 = checkout_product_1.text
print(value_checkout_product_1)
assert value_product_1 == value_checkout_product_1
print("Info about product #1 is right")

price_checkout_product_1 = driver_g.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_checkout_product_1 = price_checkout_product_1.text
print(value_price_checkout_product_1)
assert value_price_product_1 == value_price_checkout_product_1
print("Info about price is right")

summary_price = driver_g.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
value_summary_price = summary_price.text
print(value_summary_price)
item_total = "Item total: " + value_price_checkout_product_1
print(item_total)
assert value_summary_price == item_total
print("Total price is right")

"""Finishing"""
finish_btn = driver_g.find_element(By.XPATH, "//*[@id='finish']")
finish_btn.send_keys(Keys.ENTER)
print("Thank You")


