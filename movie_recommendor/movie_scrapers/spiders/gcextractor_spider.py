import scrapy
import json

class GenreSpider(scrapy.Spider):
    name = "genre"
    start_urls = [
        'https://www.imdb.com/search/title/',
    ]

    def parse(self, response):
        genres1 = response.xpath('//input[@name = "genres"]/..//label/text()').extract()
        genres = []
        for genre in genres1:
            genres.append(genre.strip())
        genres.sort()
        print(genres)
        data = {}
        data['genres'] = genres
        with open('data/genre', 'w') as outfile:
            json.dump(data, outfile)

class CategorySpider(scrapy.Spider):
    name = "category"
    start_urls = [
        'https://www.imdb.com/search/title/',
    ]

    def parse(self, response):
        cat1 = response.xpath('//input[@name = "title_type"]/..//label/text()').extract()
        cats = []
        for c in cat1:
            cats.append(c.strip())
        cats.sort()
        print(cats)
        data = {}
        data['Categories'] = cats
        with open('data/categories', 'w') as outfile:
            json.dump(data, outfile)
