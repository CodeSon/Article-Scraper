from webbrowser import get
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from article_scraper.items import Article
import time



class WikipediaSpider(CrawlSpider):
    name = 'wikipedia'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/Elizabeth_II']

    ## creating rules for the crawler to follow internal urls but excluse random common pages
    rules = [Rule(LinkExtractor(allow=r'wiki/((?!:).)*$'), callback='parse_info',
     follow=True)]

    def parse_info(self, response):
        article = Article()
        
        article['title'] =  response.xpath('//h1/text()').get() or response.xpath('//h1/i/text()').get()
        #time.sleep(2)
        article['url'] = response.url
        #time.sleep(2)
        article['lastUpdated'] = response.xpath('//li[@id="footer-info-lastmod"]/text()').get()
        return article
