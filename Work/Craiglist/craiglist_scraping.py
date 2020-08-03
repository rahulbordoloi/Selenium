## Craiglist Scraping using Selenium Python
## Documentation -> https://www.selenium.dev/documentation/en/

# Importing Neccessary Libraries
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

class CraiglistScraper:
    
    # Constructor
    def __init__(self, location, min_price, max_price):

        self.location = location
        self.min_price = min_price
        self.max_price = max_price
        self.url = f'https://{self.location}.craigslist.org/search/sss?min_price={min_price}&max_price={max_price}'
        self.driver = webdriver.Chrome(executable_path = "C:\Personal\Work\Selenium\Drivers\chromedriver.exe")
        self.delay = 3
        self.titles = []
        self.prices = []
        self.dates = []
        self.urls = []
    
    # Load the Page associated with the URL
    def load_url(self):

        self.driver.get(self.url)
        try:
            wait = WebDriverWait(self.driver, self.delay)
            wait.until(EC.presence_of_element_located((By.ID, "searchform")))  # searchform -> the whole list of items
            print("Page is Loaded and Ready to get Parsed!")
        except TimeoutException:
            print("Loading Took too much Time! Increase Delay Amount.")

    # Extract the information from Each Card
    def extract_cards(self):

        cards = self.driver.find_elements_by_class_name("result-row")
        # print(cards)
        card_list = []
        for card in cards:
            # print(card.text)

            title = card.text.split("$")

            # print(title)
            if title[0] == '':      
                title = title[1]
            else:       
                title = title[1]

            title = title.split("\n")       # Each New Line depicts the information about an object
            price = title[0]
            title = title[-1] 

            title = title.split(" ")
            month, day = title[0], title[1]
            date = month + " " + day
            title = ' '.join(title[2:])      # Taking the Rest of String excluding 
            # print(title)

            # print("Title of the Item : {}".format(title))
            # print("Price of the Item : ${}".format(price))
            # print("Date of the Item : {} 2020".format(date))
            
            # Appending the Information into Lists
            self.titles.append(title)
            self.prices.append(price)
            self.dates.append(date)

            #card_list.append(card.text)
        # for i in card_list:     print(i)
        # return card_list
        # return titles, prices, dates

    # Extarct URLs from the Cards
    def extract_card_urls(self):

        html_page = urllib.request.urlopen(self.url)
        soup = BeautifulSoup(html_page, 'lxml')
        for link in soup.findAll("a", {"class" : "result-title hdrlnk"}):
            # print(link["href"])
            self.urls.append(link["href"])
    
    # Extract Information about the Cards
    def generate_csv(self):

        # Take out the URLs of the Cards
        self.extract_card_urls() 

        # Using Pandas DataFrame
        df = pd.DataFrame()
        df['Date'] = self.dates
        df['URL'] = self.urls
        df['Title'] = self.titles
        df['Price($)'] = self.prices
        df.to_csv('craiglist_results.csv', index = False)

        # Using File IO
        '''        
        # Initialising CSV File to Save our Results
        with open('craiglist_results.csv', 'w') as f:
            f.write("Date, Title, Price($) \n")
        
        # Store out all the information
        no_of_items = len(self.titles)
        with open('craiglist_results.csv', 'a') as f:
            for i in range(no_of_items):
                f.write(str(self.dates[i]) + "," + str(self.titles[i]) + + "," + str(self.prices[i]) + "\n")
        '''
        
    # Close the Browser Session
    def quit(self):
        self.driver.close()

    # Test Function to Print the URL 
    def test(self):
        print(self.url)

# Main Function
if __name__ == '__main__':
    
    scrapper = CraiglistScraper('sfbay', 5, 5000)
    # scrapper.test()
    scrapper.load_url()
    # scrapper.extract_card_urls()
    scrapper.extract_cards()
    scrapper.generate_csv()
    scrapper.quit()