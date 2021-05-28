from selenium import webdriver
import time

from .initial_setup.config_parser import config

class GoogleVerifier:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def _parse(self,item):
        search_string = "{} {}".format(item["name"], item["release_date"])
        search_string = search_string.replace(' ','+')
        self.driver.get('https://www.google.com/search?q='+search_string)
        
        try:
            item["glikes"] = int("".join([x for x in self.driver.find_element_by_xpath("//div[@class='srBp4 Vrkhme']").text if x.isdigit()]),10)
        except:
            item["glikes"] = None

        try:
            item["grating"] = float(self.driver.find_element_by_xpath("//div[@class='xt8Uw TVtOme']").text)
        except:
            item["grating"] = None

        time.sleep(1)

    def verify(self,item):
        self._parse(item)
        if config.user["gmode"] == "s": # strict
            if item["glikes"] != None and item["glikes"] >= config.user["min_google_likes"] and item["grating"] != None and item["grating"] >= config.user["min_google_rating"]:
                return True
            else:
                return False
        
        else:
            raise RuntimeError("Invalid gmode in config/user.json")
    
    def __del__(self):
        self.driver.quit()
