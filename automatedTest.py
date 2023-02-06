import selenium
from selenium import webdriver
import time
def automatedTest():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    #browser = Chrome()
    browser.get('http://127.0.0.1:8000/')

    button = browser.find_element("id","register")
    time.sleep(5)
    button.click()
    time.sleep(5)

    email = browser.find_element("id", "email")
    email.send_keys("Tester12@gmail.com")
    username = browser.find_element("id", "username")
    username.send_keys("Tester12")
    password = browser.find_element("id","password")
    password.send_keys("AutOmAtEdTeSt1234")
    time.sleep(5)
    submit = browser.find_element("id", "submit")
    return "Test Passed!"

if __name__ == '__main__':
    print(automatedTest())
