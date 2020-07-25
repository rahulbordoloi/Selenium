from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = "C:\Personal\Work\Selenium\Drivers\chromedriver.exe")

driver.get("http://demo.automationtesting.in/")  # AT (Automation Testing)
print(driver.title)

driver.get("https://rahulbordoloi.me/")     # PW (Personal Website)
print(driver.title)

time.sleep(5)
driver.back()                  # Navigate (Go) to the Previous Page
print(driver.title)            # AT

time.sleep(5)
driver.forward()               # Navigate (Go) to the Next Page 
print(driver.title)            # PW

