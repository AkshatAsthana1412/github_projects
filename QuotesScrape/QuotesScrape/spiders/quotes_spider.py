import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes_spider'
    count = 0
    # start_urls = [
    # 'http://quotes.toscrape.com/page/1/',
    #   'http://quotes.toscrape.com/page/2/',
    # ]  alternative to the start_requests function

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        quotes = response.css('div.quote')
        for quote in quotes:
            yield {
                'page': self.count+1,
                'quote': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall()
            }
        self.count += 1
        next_page = response.css('li.next a::attr(href)').get()
        if self.count < 5 and next_page is not None: #scrape first 5 pages only
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
            response.follow()
        
        #we can also use the following for scraping all pages:
        # yield from response.follow_all(css='li.next a', callback=self.parse)
