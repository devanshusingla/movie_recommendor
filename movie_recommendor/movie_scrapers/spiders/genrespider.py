import scrapy
import json

class GenreSpider(scrapy.Spider):
    name = "genre"
    start_urls = [
        'https://www.imdb.com/feature/genre/',
    ]

    def parse(self, response):
        genres1 = response.xpath('//div[@class="article"][6]//a/text()').extract()
        genres = []
        for genre in genres1:
            genres.append(genre.strip())
        genres.sort()
        print(genres)
        data = {}
        data['genres'] = genres
        with open('data/genre', 'w') as outfile:
            json.dump(data, outfile)