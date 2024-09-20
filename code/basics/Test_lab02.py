from selenium import webdriver
from datetime import time

def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    print(driver.title)
    driver.back()
    driver.get("https://www.bing.com")
    driver.forward()
    driver.refresh()
    time.sleep(15)
    driver.quit()


