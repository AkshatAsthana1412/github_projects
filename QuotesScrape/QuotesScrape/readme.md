## A simple web scraper that scrapes quotes from http://quotes.toscrape.com - automatic!

### Technologies used:
* **Python**
* **Scrapy**

### Description
Uses a single spider 'quotes_spider' to crawl the pages, Scrapes the first five pages only (can be changed).

To run the spider, install python and scrapy then navigate to the root folder and run the following command in the console:
```shell
scrapy crawl quotes_spider
```

To save the result in a file (json/csv/jsonline etc.) use:
```shell
scrapy crawl quotes_spider -O file.<extension>
```


