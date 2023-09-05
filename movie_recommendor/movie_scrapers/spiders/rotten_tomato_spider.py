import scrapy
from scrapy.utils.response import open_in_browser

class RottenSpider(scrapy.Spider):
    name = "RottenSpider"

    def __init__(self,urls):
        self.start_urls = urls

    def parse_rt(self, response):
        critic_score = response.xpath('//score-board/@tomatometerscore').extract()[0]
        audience_score = response.xpath('//score-board/@audiencescore').extract()[0]
        synopsis = response.xpath('//p[@data-qa = "movie-info-synopsis"]/text()').extract()[0]
        genres = response.xpath('//li[@class = "info-item"]/p/span[@class = "genre"]/text()').extract()[0]
        print(critic_score, audience_score, synopsis,genres)


    def parse(self, response):
        next_page = response.xpath('//div[@class = "egMi0 kCrYT"]/a/@href').extract()[0]
        next_page = response.urljoin(next_page)
        yield scrapy.Request(next_page, callback=self.parse_rt)
        