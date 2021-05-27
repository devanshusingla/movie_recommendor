# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class Movie(Item):
    name = Field()
    release_date = Field()
    grating = Field()
    glikes = Field()
    selected = Field()
