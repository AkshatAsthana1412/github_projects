import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from books_scrape.items import BooksScrapeItem
import re

class CrawlSpiderSpider(CrawlSpider):
    name = 'crawl_spider'
    allowed_domains = ['books.toscrape.com']
    # start_urls = ['http://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(allow=r'catalogue/'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        yield scrapy.Request('http://books.toscrape.com/')

    def parse_item(self, response):
        if response.xpath(r'//div[@class="col-sm-6 product_main"]') is not None:
            title = response.xpath(r'//div[@class="col-sm-6 product_main"]/h1/text()').get()
            price = response.xpath(r'//div[@class="col-sm-6 product_main"]/p[@class="price_color"]/text()').get()
            rating = response.xpath(r'string(//div[@class="col-sm-6 product_main"]/p[contains(@class,"star-rating")]/@class)').get()
            availability = response.xpath(r'//div[@class="col-sm-6 product_main"]/p[@class="instock availability"]/text()').re(r'\S+')
            
            if rating:
                new_rating = re.match('^star-rating (\w+)', rating).group(1)
            else:
                new_rating = rating

            item = BooksScrapeItem()
            item['title'] = title
            item['price'] = price
            item['rating'] = new_rating
            item['availability'] = ''.join(availability)
            yield item
        else:
            print("Null record!!")