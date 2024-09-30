#Ebay_search_16GB and print all heading that founded
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    Search_btn = driver.find_element(By.XPATH,"//input[@type='text']")
    Search_btn.send_keys("16 GB")
    Search_btn_submit = driver.find_element(By.XPATH,"//input[@type = 'submit']")
    Search_btn_submit.click()
    time.sleep(5)

    list_results = driver.find_elements(By.XPATH,"//span[@role='heading']")
    for i in list_results:
        print(i.text)
    time.sleep(5)
    driver.quit()