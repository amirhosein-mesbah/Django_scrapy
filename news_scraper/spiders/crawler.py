import scrapy
from news_scraper.items import NewsScraperItem
from scrapy.http import Request
from scrapy.loader import ItemLoader

class CrawlerSpider(scrapy.Spider):

    name = 'crawler'
    allowed_domains = ['www.khabaronline.ir']

    def __init__(self, url, numofpages):
        self.numofpages = numofpages
        if not url:
            url = 'https://www.khabaronline.ir/archive'
        self.start_urls = [url]


    def parse(self, response):
        urls = response.xpath('//*[@class="desc"]/h3/a/@href').extract()
        for url in urls:
            absulote_url = response.urljoin(url)
            yield Request(absulote_url, callback=self.parse_news)

        # next page url extraction
        NUMBERofPAGES = self.numofpages
        while NUMBERofPAGES > 0:
            NUMBERofPAGES = NUMBERofPAGES - 1
            next_page_url = response.xpath('//*[@class="page-item "][last()]/a/@href').extract_first()
            absolute_next_page_url = response.urljoin(next_page_url)
            Request(absolute_next_page_url)


    def parse_news(self, response):

        url = response.url
        title = response.xpath('//h1[@class="title"]/a/text()').extract_first()
        summary = response.xpath('//p[@class="summary introtext"]/text()').extract_first()
        date = response.xpath('//div[contains(@class, "item-date")]/span/text()').extract_first()
        tags = response.xpath('//section[@class="box tags"]/div/ul/li/a/text()').extract()
        code = response.xpath('//div[@class="item-code"]/span/text()').extract_first()

        paragraphs = response.xpath('//div[@class="item-text"]/p[position() != last()]/text()').extract()
        text = ""
        for paragraph in paragraphs:
            text += paragraph + "\n"

        item = NewsScraperItem(url=url, title=title, summary=summary, date=date, tags=tags, code=code, text=text)
        item.save()
