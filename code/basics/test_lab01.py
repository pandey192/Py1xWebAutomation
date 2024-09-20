from selenium import webdriver
from datetime import time
import logging

def test_open_login():

    chrome_options = webdriver.ChromeOptions()
    #gave some extra argument or extension or anything to Chrome
    #Chrome options -  Chrome with the etension, window Sixe Proxy, JS disable
    extension_path = "/Users/apple/Downloads/addblocker1x.crx"
    chrome_options.add_extension(extension_path)
    driver = webdriver.Chrome(options=chrome_options)
    LOGGER = logging.getLogger(__name__)
    driver.get("https://google.com")
    driver.maximize_window()
    time.sleep(2000)


#driver.close() - Close will close the current tab or window not close the other tab and Session id != null
#driver.quit() -  Close the all tab or Close the whole browser and Session == None
#drvier_ navigate().to(String url) - NOT Exist in python