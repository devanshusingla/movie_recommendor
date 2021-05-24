import scrapy
import json

class GenreSpider(scrapy.Spider):
    name = "genre"
    start_urls = [
        'https://www.imdb.com/feature/genre/',
    ]

    def parse(self, response):
        genres = response.xpath('//div[@class="widget_image"]/div[@class="image"]/a/img[@class="pri_image"]/@title').extract()
        print(genres)
        data = {}
        data['genres'] = genres
        with open('../../data/genre', 'w') as outfile:
            json.dump(data, outfile)