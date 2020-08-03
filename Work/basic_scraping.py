# Importing Libraries
from selenium import webdriver

# Initialising Chrome
driver = webdriver.Chrome(executable_path = "C:\Personal\Work\Selenium\Drivers\chromedriver.exe")

# Initialising Page Information
MAX_PAGE_NUM = 5
MAX_PAGE_DIG = 3

# Initialising CSV File to Save our Results
with open('basic_crawling.csv', 'w') as f:
    f.write("Buyer, Price \n")

# For loop to loop through all the pages of that website
for i in range(1, MAX_PAGE_NUM + 1):
    page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i)
    # print(page_num)
    url = "http://econpy.pythonanywhere.com/ex/" + page_num + ".html"    # Address -> http://econpy.pythonanywhere.com/ex/001.html
    # print(url)

    # Extracting Information from the URL
    driver.get(url)

    # Extracting lists of "buyers" and "prices" based on xpath.
    buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
    prices = driver.find_elements_by_xpath('//span[@class="item-price"]')
    num_page_items = len(buyers)

    # Store out all of the buyers and prices on CSV
    num_page_items = len(buyers)
    with open('basic_crawling.csv', 'a') as f:
        for i in range(num_page_items):
            f.write(buyers[i].text + "," + prices[i].text + "\n")

# Close Browser
driver.close()