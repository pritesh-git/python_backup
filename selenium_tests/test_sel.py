import os
from selenium import webdriver
from time import sleep
from loginScreen import *
from switchTo_menu import *
from selenium.webdriver.support.select import Select

driver_location = "/usr/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"
option = webdriver.ChromeOptions()
option.binary_location = binary_location
option.add_argument("window-size=900,700")
option.add_argument("window-position=300,100")
option.add_argument('--incognito')
driver = webdriver.Chrome(executable_path=driver_location, options=option)
driver.get("http://demo.automationtesting.in/")

loginScreen(driver, sleep)

registerScreen(driver, Select, os)

switchToAlert(driver, sleep)

# switchToWindow(driver, sleep)

switchToIframe(driver, sleep)

sleep(2)

# driver.close()    #will close only parent tab
driver.quit()  # will close all tab in focused browser
