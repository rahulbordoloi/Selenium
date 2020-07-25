from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = "C:\Personal\Work\Selenium\Drivers\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")

userElement = driver.find_element_by_id("user-name")  # can select by "name" too
print(userElement.is_displayed())           # Returns True or False based on Element's Status
print(userElement.is_enabled())             # Returns True or False based on Element's Status

pwElement = driver.find_element_by_id("password")
print(pwElement.is_displayed())           # Returns True or False based on Element's Status
print(pwElement.is_enabled())             # Returns True or False based on Element's Status

userElement.send_keys("standard_user")    # Automated Entry of Username
pwElement.send_keys("secret_sauce")       # Automated Entry of Password
signInElement = driver.find_element_by_id("login-button").click()  # Click on the Button

try:

    roundTripRadio = driver.find_element_by_css_selector("input[value=roundtrip]")   # CSS Selctor
    print("Status of the Round Trip Radio Button :", roundTripRadio.is_displayed())  # Returns Status of Round Trip Button
    print(roundTripRadio.is_selected())            # Returns if the Round Trip Radio Button is Selected

    oneTripRadio = driver.find_element_by_css_selector("input[value=oneway]")
    print("Status of the One Way Radio Button :", oneTripRadio.is_displayed())  # Returns Status of One Trip Button
    print(roundTripRadio.is_selected())            # Returns if the One Trip Radio Button is Selected

except:
    print("Element Not Found!")
