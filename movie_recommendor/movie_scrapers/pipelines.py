# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from ..google_verifier import GoogleVerifier


class MovieScrapersPipeline:
    def __init__(self):
        self.ids_seen = set()
        self.gv = GoogleVerifier()
        self.f = open('data/movies.jl', 'w')
    
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if (adapter['name'],adapter['release_date']) in self.ids_seen:
            DropItem(f"Dupticate item found: {item!r}")
        else:
            self.ids_seen.add((adapter['name'],adapter['release_date']))
            if self.gv.verify(item):
                self.f.write(json.dumps(ItemAdapter(item).asdict())+'\n')
                return item
            else:
                DropItem('Failed as a good movie by given criterion')
    
    def __del__(self):
        self.f.close()