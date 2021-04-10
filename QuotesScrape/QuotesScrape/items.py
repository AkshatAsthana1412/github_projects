# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import Join

class QuotesScrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = scrapy.Field()
    quote = scrapy.Field()
    tags = scrapy.Field()

class QuoteLoader(ItemLoader):
    tags_out = Join('|')