from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path = "C:\Personal\Work\Selenium\Drivers\chromedriver.exe")

driver.implicitly_wait(5) # For the Whole Driver
driver.maximize_window()
driver.get("https://www.expedia.com/")   

driver.find_element_by_id("tab-flight-tab-hp").click()   # Flights Button
## OR
# driver.find_element(By.ID, "tab-flight-tab-hp").click()

driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")        # origin
time.sleep(2)               # For Python Code
driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")   # destination

driver.find_element(by.ID, "flight-departing-hp-flight").clear()   # To Clear the Field Out
driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("25/07/2020")
driver.find_element(by.ID, "flight-returning-hp-flight").clear()   # To Clear the Field Out
driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("12/10/2020")

driver.find_element(By.XPATH, '//*[@id="gcw-flights-form-hp-flight"]/div[7]/label/button').click() # Submit Button

# Explicit Wait
wait = WebDriverWait(driver, 10)  # 10 -> Maximum Timeout
driver.find_element(by.XPATH, "//*[@id-'stopFilter_stops-0']")    # Select Non-Stops Flight
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gcw-flights-form-hp-flight"]/div[7]/label/button'))) # waits until the element becomes visible in the page
element.click()

time.sleep(3)
driver.quit()
