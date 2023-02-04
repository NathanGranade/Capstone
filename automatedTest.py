import selenium
from selenium.webdriver import Chrome
import time

browser = Chrome()
browser.get('http://127.0.0.1:8000/')

button = browser.find_element("link text","sign up")
time.sleep(5)
button.click()
time.sleep(5)

email = browser.find_element("id", "email")
email.send_keys("Tester1@gmail.com")
time.sleep(5)

