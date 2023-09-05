from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class GoogleRating:
    def __init__(self, name, release_date):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        search_string = "{} {}".format(name, release_date)
        search_string = search_string.replace(' ','+')
        self.parse(search_string)

    def parse(self, search_string):
        self.driver.get('https://www.google.com/search?q='+search_string)
        
        try:
            glikes = int("".join([x for x in self.driver.find_element(by= 'xpath', value = "//div[@class='srBp4 Vrkhme']/div/span").text if x.isdigit()]),10)
        except:
            glikes = None
        
        try:
            grating = float(self.driver.find_element(by= 'xpath', value ="//div[@class='xt8Uw q8U8x']").text)
        except:
            grating = None

        print(glikes, grating)

    
    def __del__(self):
        self.driver.quit()
