from django.shortcuts import render
from news_scraper.spiders.crawler import CrawlerSpider
from scrapy.utils.project import get_project_settings
from scrapyscript import Job, Processor
import json
from .models import NewsModel



def home(request):
    """ Home page view """
    return render(request, 'index.html')

def run_crawler(url, numofpages):
    newsJob = Job(CrawlerSpider, url=url, numofpages=numofpages)
    processor = Processor(get_project_settings())
    processor.run([newsJob])
    return None

def result(request):
    """ Result page view """
    url = request.GET['url']
    numofpages = int(request.GET['numofpages'])
    day = request.GET['day']
    month = request.GET['month']
    year = request.GET['year']

    if not((day == '') and (month == '') and (year == '')):
        url = url + '/page/archive.xhtml?wide=0&ms=0&pi=1&dy='+str(day)+'&mn='+str(month)+'&yr='+str(year)
    run_crawler(url, numofpages)

    # Fetching scraped data from django database
    data = NewsModel.objects.all().values()

    # pay attention:
    # in here you can import your mongodb and save the data into mongo database
    with open('data.json', 'w') as outfile:
        json.dump(list(data), outfile)

    return render(request, 'result.html', {'result':str(len(data))+" new document scraped until now!"})
