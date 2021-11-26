## Books Scraper

Scrapes book information from the website: [http://books.toscrape.com/]

The scraped content is structured in the following way:
- title
- price
- rating
- availability

the scraped information is yielded in item objects which could be stored in json, jsonlines, csv etc formats as specified in the console using the command:

`scrapy crawl crawl_spider -o json`

the scraped information could then be used to run analytics.
