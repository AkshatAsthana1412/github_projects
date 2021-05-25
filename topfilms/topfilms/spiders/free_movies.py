from scrapy import Spider, Request
import logging
from topfilms.items import FreeMovie

logger = logging.getLogger('spider1')
class FreeMovies(Spider):
    name='free_movies'
    start_urls = [
        'https://www.themoviedb.org/remote/panel?panel=free_scroller&group=movie'
    ]

    def parse(self, response):
        css_sel = 'div.content > h2 > a'
        for a_tag in response.css(css_sel):
            title = a_tag.css('::attr(title)').get()
            logger.info(title)
            movie_link = a_tag.css('::attr(href)').get()
            # yield Request(f'https://www.themoviedb.org/{movie_link}', callback=self.parse_movie)
            yield response.follow(movie_link, callback=self.parse_movie)

    def parse_movie(self, response):
        title_selector = '//div[@class="title ott_true"]/h2/a/text()'
        genres_selector = 'div>span.genres>a::text'
        percent_selector = 'div.user_score_chart::attr(data-percent)'
        overview_selector = 'div.overview>p::text'
        item = FreeMovie()
        item['title'] = response.xpath(title_selector).get()
        item['tags'] = response.css(genres_selector).getall()
        item['user_score'] = response.css(percent_selector).get()
        item['overview'] = response.css(overview_selector).get()
        yield item

        