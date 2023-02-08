from selenium import webdriver
import time
def automatedTest():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    
    browser.get('http://127.0.0.1:8000/')

    button = browser.find_element("id","register")
    time.sleep(5)
    button.click()
    time.sleep(5)

    email = browser.find_element("id", "email")
    email.send_keys("DEMO@gmail.com")
    username = browser.find_element("id", "username")
    username.send_keys("DEMO")
    password = browser.find_element("id","password")
    password.send_keys("ThIsIsADemOPassWord")
    time.sleep(5)
    submit = browser.find_element("id", "submit")
    submit.click()
    time.sleep(5)
    return "Test Passed!"

if __name__ == '__main__':
    print(automatedTest())
