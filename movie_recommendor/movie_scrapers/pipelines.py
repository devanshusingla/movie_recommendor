# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class MovieScrapersPipeline:
    def __init__(self):
        self.ids_seen = set()
    
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if (adapter['name'],adapter['release_date']) in self.ids_seen:
            DropItem(f"Dupticate item found: {item!r}")
        else:
            self.ids_seen.add((adapter['name'],adapter['release_date']))
            return item