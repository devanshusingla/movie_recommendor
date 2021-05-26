from scrapy.crawler import CrawlerProcess
from movie_recommendor.movie_scrapers.spiders.gcextractor_spider import GenreSpider, CategorySpider
print("Extracing genre.....")
process = CrawlerProcess()
process.crawl(GenreSpider)
process.crawl(CategorySpider)
process.start()