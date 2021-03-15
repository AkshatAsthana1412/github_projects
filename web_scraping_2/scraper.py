import scrapy

class BrickSetSpider(scrapy.Spider):
    name = 'brickset_spider'
    start_urls = ['https://brickset.com/sets/year-2019']
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36',
    }

    def parse(self, response):
        SET_SELECTOR = '.set'
        PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
        for brickset in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'h1 ::text'
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(), 
                'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
            }

    # More code can be added to make the spider follow the urls to the next pages until 
    # the last page
