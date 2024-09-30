#app.vwo.com_automate
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_vwo_login_positive():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    email_btn = driver.find_element(By.ID,"login-username")
    email_btn.send_keys("pyatb3x@wingify.com")
    Password_btn = driver.find_element(By.ID,"login-password")
    Password_btn.send_keys("Wingify@1234")
    time.sleep(2)
    signin_btn = driver.find_element(By.ID,"js-login-btn")
    signin_btn.click()

    time.sleep(10)
    driver.quit()

def test_vwo_login_Negative():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    #email_btn = driver.find_element(By.ID,"login-username")
    email_btn = driver.find_element(By.XPATH, "//input[@type='email']")
    email_btn.send_keys("pyatb3x@wingify.com")
    #Password_btn = driver.find_element(By.ID,"login-password")
    Password_btn = driver.find_element(By.XPATH, "//input[@type='password']")
    Password_btn.send_keys("Whasgdfingify@1234")
    time.sleep(2)
    signin_btn = driver.find_element(By.ID,"js-login-btn")
    signin_btn.click()

    time.sleep(10)
    driver.quit()
