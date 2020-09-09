# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy_djangoitem import DjangoItem
from scrapy_app.models import NewsModel

class NewsScraperItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()

    django_model = NewsModel
    #
    # url = scrapy.Field()
    # title = scrapy.Field()
    # summary = scrapy.Field()
    # date = scrapy.Field()
    # tags = scrapy.Field()
    # text = scrapy.Field()
    # code = scrapy.Field()
