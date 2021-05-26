import scrapy
from selenium import webdriver
from itertools import combinations

class Movie_Spider(scrapy.Spider):
    def __init__(self, config):
        self.name = 'movie_spider'
        self.config = config

        driver = webdriver.Chrome()
        driver.get("https://www.imdb.com/search/title/")
        self._fill_form(driver)
    
    def _fill_form(self, driver):
        div_list = driver.find_elements_by_xpath("//div[@class='clause']")
        for div in div_list:
            pass