# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import Join, MapCompose, Compose

class QuotesScrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = scrapy.Field()
    quote = scrapy.Field()
    tags = scrapy.Field()

class QuoteLoader(ItemLoader):
<<<<<<< HEAD
    g = lambda x: bytes(x, 'utf-8')
    f = lambda x: x.decode('utf-8')
    author_in = MapCompose(g)
    quote_in = MapCompose(g)
    tags_in = MapCompose(g)
    author_out = MapCompose(f)
    quote_out = MapCompose(f)
    tags_out = Compose(MapCompose(f), Join('|'))
    # tags_out = Join('|')
=======
    tags_out = Join('|')
>>>>>>> 61da4546e1d275915280585b0f156e65989ad8ae
