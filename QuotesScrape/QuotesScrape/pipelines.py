# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3 as lite
import json

class QuotesScrapePipeline:

    def open_spider(self, spider):
        self.file = open('Results.jl', 'w', newline='')

    def close_spider(self, spider):
        self.file.close()
        
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        line = json.dumps(adapter.asdict(), ensure_ascii=True) + '\n'
        self.file.write(line)
        print('Item Scraped!')
        return item
