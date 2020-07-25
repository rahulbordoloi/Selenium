from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = "C:\Personal\Work\Selenium\Drivers\chromedriver.exe")
#driver = webdriver.Firefox(executable_path = "C:\Personal\Work\Selenium\Drivers\geckodriver.exe")
#driver = webdriver.Ie(executable_path = "path_to_IE_Web_Driver")
driver.get("https://rahulbordoloi.me")

print(driver.title)             # Title of the Page
print(driver.current_url)       # Return the URL of the Page
print(driver.page_source)       # HTMl Code of the Page
driver.close()                  # Close the Browser