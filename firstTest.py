from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service('path/to/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://tutorialsninja.com/demo/')

elem = driver.find_element(By.NAME, "search")
elem.clear()
elem.send_keys('iphone')
elem.send_keys(Keys.RETURN)

add_to_cart_button = driver.find_element(By.XPATH, "//div[@class='product-layout product-grid col-lg-3 col-md-3 col-sm-6 col-xs-12']//button[1]")
time.sleep(2)
add_to_cart_button.click()

cart_total_button = driver.find_element(By.ID, 'cart')
time.sleep(2)
cart_total_button.click()

view_cart_link = driver.find_element(By.XPATH, "//body//header//div[@id='cart']//div//a[1]")
time.sleep(2)
view_cart_link.click()

assert "product 11" in driver.page_source


