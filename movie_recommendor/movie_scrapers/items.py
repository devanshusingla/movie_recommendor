# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class Movie(Item):
    movie_id = Field()
    name = Field()
    imdbLikes = Field()
    img_url = Field()
    release_date = Field()
    glikes = Field()

class gclData(Item):
    data = Field()
