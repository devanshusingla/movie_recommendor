import scrapy
from scrapy.utils.response import open_in_browser
from ..items import Movie
from ..pipelines import IMDbPipeline

class IMDbSpider(scrapy.Spider):
  name = "imdbspider"
  
  def __init__(self,**kwargs):
    self.start_urls = kwargs["urls"]
    self.movieLimit = kwargs["movieLimit"]
    self.pages = self.movieLimit//50
    self.dp = IMDbPipeline()

  def process_dates(self,dates):
        processed_dates = []
        for date in dates:
            date = date.strip("()")
            processed_dates.append(date)
        return processed_dates

  def parse(self, response, page = 0):
    movie_id = response.xpath('//div[@class = "lister list detail sub-list"]//div[@class="ratings-bar"]/div[@class="inline-block ratings-user-rating"]/span/@data-tconst').extract()
    # img_url = response.xpath('//div[@class = "lister list detail sub-list"]//div[@class="lister-item-image float-left"]/a/img/@src').extract()
    movie_names = response.xpath('//div[@class = "lister list detail sub-list"]//h3[@class="lister-item-header"]/a/text()').extract()
    release_years = response.xpath('//div[@class = "lister list detail sub-list"]//h3[@class="lister-item-header"]/span[@class="lister-item-year text-muted unbold"]/text()').extract()
    imdb_rating = response.xpath('//div[@class = "lister list detail sub-list"]//div[@class="ratings-bar"]//strong/text()').extract()
    # print(img_url)
    try:
        next_page = response.xpath('//div[@class = "desc"]/a[@class="lister-page-next next-page"]/@href').extract()[0]
    except:
        next_page = None
    release_years = self.process_dates(release_years)
    for (id,mn,rd,rat) in zip(movie_id, movie_names,release_years,imdb_rating):
        print(id,mn,rd,rat)
        self.dp.process_item(Movie(name=mn, release_date=rd,imdbLikes=rat,movie_id=id))
    if page == self.pages: return
    if next_page is not None:
        print("going to next page ....")
        next_page = response.urljoin(next_page)
        yield scrapy.Request(next_page, callback=self.parse, cb_kwargs={'page': page+1})