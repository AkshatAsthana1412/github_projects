from scrapy import Spider
from QuotesScrape.items import QuotesScrapeItem, QuoteLoader
class QuoteSpider2(Spider):
    name = 'quotes_spider_1'
    page_no = 1
    start_urls = ['http://quotes.toscrape.com/page/1/',
                    ]

    def parse(self, response):
        print(f'Page No. {self.page_no}:')
        quotes = response.css('div.quote')
        for quote in quotes:
            author = quote.css('small.author::text').get()
            quote_text = quote.css('span.text::text').get()
            tags = quote.css('div.tags a.tag::text').getall()
            il = QuoteLoader(QuotesScrapeItem(), response)
            il.add_value('author', author)
            il.add_value('quote', quote_text)
            il.add_value('tags', tags)
            yield il.load_item()

        self.page_no += 1
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

