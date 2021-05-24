from scrapy.crawler import CrawlerProcess
from movie_recommendor.movie_scrapers.spiders.genrespider import GenreSpider
print("Extracing genre.....")
process = CrawlerProcess()
process.crawl(GenreSpider)
process.start()