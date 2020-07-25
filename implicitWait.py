from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\Personal\Work\Selenium\Drivers\chromedriver.exe")
driver.get("https://www.saucedemo.com/")   # assuming URL takes some time to open up

driver.implicitly_wait(10)  # wait for 10s, applicable for all the elements of the page
                            # whichever element is taking time, it'll wait max for 10s
                            # only one time applicable in the whole code

assert "Swag Labs" in driver.title, "Error in Title"

driver.find_element_by_id("user-name").send_keys("standard_user")  
driver.find_element_by_id("password").send_keys("standard_user")
driver.find_element_by_id("login-button").click()

driver.close()