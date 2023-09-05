# from scrapy.crawler import CrawlerProcess
# from twisted.internet import reactor
from scrapy.crawler import CrawlerProcess
from movie_recommendor.movie_scrapers.spiders.gcextractor_spider import preliminarySpider
from movie_recommendor.movie_scrapers.spiders.IMDb_spider import IMDbSpider
from movie_recommendor.movie_scrapers.spiders.rotten_tomato_spider import RottenSpider
from movie_recommendor.movie_scrapers.spiders.pahe_spider import PaheSpider
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(settings=get_project_settings())
# process.crawl(preliminarySpider)
process.crawl(PaheSpider, urls = ['https://pahe.li/?s=Avengers+endgame+2019'])
process.start()
# runner = CrawlerRunner()

# d = runner.crawl(preliminarySpider)
# d.addBoth(lambda _: reactor.stop())
# # settings = get_project_settings()
# reactor.run()