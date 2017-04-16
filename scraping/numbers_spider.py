

import scrapy


class movienumbersSpider(scrapy.Spider):
    name = "movienumbers"
    start_urls = ['http://www.the-numbers.com/movie/budgets/all']


    def parse(self, response):
        for w in response.xpath('//div[contains(@id,"page")]/center/table/tr'):
            yield {    'Rank' : w.xpath('./td[1]/text()').extract_first(),
                  'releasedate' : w.xpath('./td/a/text()').extract(),
                  'Movie' : w.xpath('./td/b/a/text()').extract(),
                  'ProductionBudget' : w.xpath('./td[4]/text()').extract_first(),
                  'DomesticGross' : w.xpath('./td[5]/text()').extract_first(),
                  'WorldwideGross' : w.xpath('./td[6]/text()').extract_first(),
                  }

##//*[@id="page_filling_chart"]/center/table/tbody/tr[2]/td[2]/a
