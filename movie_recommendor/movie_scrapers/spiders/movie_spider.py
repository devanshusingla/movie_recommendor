import scrapy
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from movie_recommendor.movie_scrapers.items import Movie
from movie_recommendor.movie_scrapers.pipelines import MovieScrapersPipeline
from itertools import combinations
import time

class Movie_Spider(scrapy.Spider):    
    def _fill_form(self, driver):
        div_list = driver.find_elements_by_xpath("//div[@class='clause']")
        def div_gen():
            for div in div_list:
                try:
                    yield {
                        "heading": div.find_element_by_tag_name('h3').text,
                        "body": div.find_element_by_class_name('inputs')
                    }
                except GeneratorExit:
                    return
                
                except:
                    pass
        
        divg = div_gen()
        div = next(divg)
        
        if "movie_categories" in self.config.user:
            while(div["heading"] != "Title Type"):
                div = next(divg)

            # print("\n\n",div["heading"],"\n\n")
            elements = div["body"].find_elements_by_tag_name('td')
            for e in elements:
                if e.find_element_by_tag_name('label').text in self.config.user["movie_categories"]:
                    e.find_element_by_tag_name('input').click()
        
        if "release_date" in self.config.user and self.config.user["release_date"]:
            while(div["heading"] != "Release Date"):
                div = next(divg)

            # print("\n\n",div["heading"],"\n\n")
            div["body"].find_element_by_name('release_date-min').send_keys(self.config.user["release_date"][0])
            try:
                div["body"].find_element_by_name('release_date-max').send_keys(self.config.user["release_date"][1])
            except:
                pass
        
        if "min_imdb_rating" in self.config.user or "max_imdb_rating" in self.config.user:
            while(div["heading"] != "User Rating"):
                div = next(divg)

            # print("\n\n",div["heading"],"\n\n")
            if "min_imdb_rating" in self.config.user:
                try:
                    Select(div["body"].find_element_by_name('user_rating-min')).select_by_visible_text(self.config.user["min_imdb_rating"])
                except:
                    pass

            if "max_imdb_rating" in self.config.user:
                try:
                    Select(div["body"].find_element_by_name('user_rating-max')).select_by_visible_text(self.config.user["max_imdb_rating"])
                except:
                    pass
        
        while(div["heading"] != "Genres"):
            div = next(divg)

        # print("\n\n",div["heading"],"\n\n")
        genre_list = div["body"].find_elements_by_tag_name('td')
        
        if "language" in self.config.user:
            while(div["heading"] != "Languages"):
                div = next(divg)

            print("\n\n",div["heading"],"\n\n")
            try:
                Select(div["body"].find_element_by_tag_name('select')).select_by_visible_text(self.config.user["language"])
            except:
                pass
        
        if "adult_titles_included" in self.config.user and self.config.user["adult_titles_included"]:
            while(div["heading"] != "Adult Titles"):
                div = next(divg)

            # print("\n\n",div["heading"],"\n\n")
            div["body"].find_element_by_xpath("//input[@id='adult|include']").click()

        return genre_list

    def _extract_link(self, driver, genre_combination, genre_list):
        checkboxes = [x.find_element_by_tag_name('input') for x in genre_list if x.find_element_by_tag_name('label').text in genre_combination]
        for checkbox in checkboxes:
            checkbox.click()

        submit_button = driver.find_element_by_xpath("//button[text()='Search']")
        ActionChains(driver).key_down(Keys.CONTROL).click(submit_button).key_up(Keys.CONTROL).perform()

        driver.switch_to.window(driver.window_handles[1])
        link = driver.current_url
        print("\n\n",link,"\n\n")
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        for checkbox in checkboxes:
            checkbox.click()

        return link
    
    def __init__(self, config):
        self.name = 'movie_spider'
        self.config = config

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.imdb.com/search/title/")
        genre_list = self._fill_form(driver)

        genre_combinations = [(x,) for x in self.config.user["genre"]]
        if len(self.config.user["genre"]) >= 2:
            genre_combinations += combinations(self.config.user["genre"], 2)

        if len(self.config.user["genre"]) >= 3:
            genre_combinations += combinations(self.config.user["genre"], 3)
        
        self.start_urls = [self._extract_link(driver, genre_combination, genre_list) for genre_combination in genre_combinations]
        print("\n\n",self.start_urls,"\n\n")
        self.dp = MovieScrapersPipeline()
        driver.quit()
    
    def process_dates(self,dates):
        processed_dates = []
        for date in dates:
            date = date.split()
            tdate = ""
            if len(date) == 2:
                tdate = date[1]
            else:
                tdate = date[0]
            processed_dates.append(tdate)
        return processed_dates


    
    def parse(self, response, index = 0):
        #print("\n")
        #print("i = "+str(index))
        #print("\n")
        imdb_lim = self.config.app['imdb_search_limit']
        movie_names = response.xpath('//div[@class = "lister list detail sub-list"]//h3[@class="lister-item-header"]/a/text()').extract()
        release_years = response.xpath('//div[@class = "lister list detail sub-list"]//h3[@class="lister-item-header"]/span[@class="lister-item-year text-muted unbold"]/text()').extract()
        index+=len(movie_names)
        if(len(movie_names)<50):
            next_page = None
        else:
            next_page = response.xpath('//div[@class = "desc"]/a[@class="lister-page-next next-page"]/@href').extract()[0]
        if(index>imdb_lim):
            del movie_names[-index+imdb_lim:]
            del release_years[-index+imdb_lim:]
            index = 0
            next_page =None
        else:
            next_page = response.xpath('//div[@class = "desc"]/a[@class="lister-page-next next-page"]/@href').extract()[0]
        #print("\n")
        #print(movie_names)
        #print("\n")
        release_years = self.process_dates(release_years)
        #print(len(movie_names))
        for (m,r) in zip(movie_names, release_years):
            yield self.dp.process_item(Movie(name=m, release_date=r),self)
        print(next_page)
        if next_page is not None:
            print("going to next page ....")
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse, cb_kwargs={'index':index})
        else:
            index = 0
        
        if(index>=imdb_lim):
            index=0
            pass

