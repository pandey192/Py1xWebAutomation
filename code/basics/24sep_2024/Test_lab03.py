import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appoitnment_btn = driver.find_element(By.ID,"btn-make-appointment")
    make_appoitnment_btn.click()
    print(driver.current_url) #verification of the url #assert

    #assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    username_btn = driver.find_element(By.ID,"txt-username")
    username_btn.send_keys("John Doe")
    password_btn = driver.find_element(By.ID,"txt-password")
    password_btn.send_keys("ThisIsNotAPassword")
    submit_btn = driver.find_element(By.ID,"btn-login")
    submit_btn.click()
    #assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment","Error wrong Url"
    time.sleep(5)
    driver.quit()

def test_open_login_Edge():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appoitnment_btn = driver.find_element(By.ID,"btn-make-appointment")
    make_appoitnment_btn.click()
    print(driver.current_url) #verification of the url #assert

    #assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    username_btn = driver.find_element(By.ID,"txt-username")
    username_btn.send_keys("John Doe")
    password_btn = driver.find_element(By.ID,"txt-password")
    password_btn.send_keys("ThisIsNotAPassword")
    submit_btn = driver.find_element(By.ID,"btn-login")
    submit_btn.click()
    #assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment","Error wrong Url"
    time.sleep(5)
    driver.quit()