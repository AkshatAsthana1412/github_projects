# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TopfilmsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titles = scrapy.Field()
    channel = scrapy.Field()
    start_ts = scrapy.Field()
    film_date_long = scrapy.Field()
    film_date_short = scrapy.Field()
    genre = scrapy.Field()
    plot = scrapy.Field()
    rating = scrapy.Field()
    tmdb_link = scrapy.Field()
    release_date = scrapy.Field()
    nb_votes = scrapy.Field()


class FreeMovie(scrapy.Item):
    title = scrapy.Field()
    tags = scrapy.Field()
    overview = scrapy.Field()
    user_score = scrapy.Field()
