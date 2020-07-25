from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = "C:\Personal\Work\Selenium\Drivers\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)             # Title of the Page
print(driver.current_url)       # Return the URL of the Page

# Get the Element ID from the WebPage Inspect Element and Copy it's xPath
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()   # Click to go to the next page

time.sleep(5)                    # Halt Execution for 5s

driver.close()                   # Close Currently Focussed Browser (Tab)
driver.quit()                    # Closes all the Browsers (Tabs)