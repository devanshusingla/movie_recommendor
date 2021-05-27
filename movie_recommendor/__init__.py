from .initial_setup import *

from twisted.internet import reactor
from scrapy import signals
from scrapy.crawler import Crawler, CrawlerProcess
from movie_recommendor.movie_scrapers.spiders.gcextractor_spider import GenreSpider, CategorySpider
from .movie_scrapers.spiders.movie_spider import Movie_Spider

from .google_verifier import GoogleVerifier

gv = GoogleVerifier()

crawler = Crawler(Movie_Spider)
crawler.signals.connect(gv.verify, signals.item_scraped)
crawler.signals.connect(gv.print, signals.spider_closed)

process = CrawlerProcess()
process.crawl(GenreSpider)
process.crawl(CategorySpider)
process.crawl(crawler, config = config_parser.config)
process.start()