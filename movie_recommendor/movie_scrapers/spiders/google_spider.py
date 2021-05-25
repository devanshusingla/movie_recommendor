import scrapy

class GoogleSpider(scrapy.Spider):
    def __init__(self, movie):
        self.name = ""
        self.start_urls = []
        self.movie = movie
        scrapy.Spider.__init__(self)
    
    def parse(self, response, **kwargs):
        
        return self.movie