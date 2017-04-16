import scrapy
import pandas as pd
df_movie = pd.read_csv('/Users/abhisekswain/ds/metis/metisgh/nyc17_ds10/student_submissions/projects/02-luther/luther/luther/movie_list_data.csv')
movie_list = df_movie.link
#print movie_list

class ImdbSpider(scrapy.Spider):
    name = "moviedetails"
    start_urls = ['http://www.imdb.com/title/tt0110912/']

    def parse(self, response):

        yield {
        'title': response.xpath('//h1/text()').extract()[0].strip(),
        'user_rating': response.xpath('//div[contains(@class, "imdb")]/div[1]/strong/span/text()').extract(),
        'genre': response.xpath('//div[@id="titleStoryLine"]/div[4]/a/text()').extract(),
        'mpaa_rating' : response.xpath('//div[contains(@class, "article")]/div[5]/span[1]/text()').extract(),
        'meta_score': response.xpath('//div[contains(@class, "metacriticScore")]/span/text()').extract()[0],
        'ratingnum': response.xpath('//div[contains(@class,"imdb")]/a/span/text()').extract(),
        'budget' : response.xpath('//div[contains(@class,"article")]/div[7]/text()[2]').extract(),
        'gross' : response.xpath('//div[contains(@class,"article")]/div[9]/text()[2]').extract()
        }

        for i in movie_list:
            next_page = "http://www.imdb.com"+ i
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

#//*[@id="title-overview-widget"]/div[2]/div[2]/div/div[2]/div[2]/div/a[1]/span
