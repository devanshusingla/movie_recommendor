from .initial_setup import *
from scrapy.crawler import CrawlerProcess
from .movie_scrapers.spiders.movie_spider import Movie_Spider

config = config_parser.config

process = CrawlerProcess()
process.crawl(Movie_Spider, config = config)
process.start()