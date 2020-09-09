from django.db import models
from django_mysql.models import ListCharField

class NewsData(models.Model):
    """ News Dataset Model """
    url = models.CharField(max_length=10)
    title = models.TextField()
    summary = models.TextField(blank=True)
    date = models.CharField(max_length=20)
    tags = ListCharField(base_field=models.CharField(max_length=20),max_length=(10*21))
    text = models.TextField(blank=True)
    code = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Scrapy Django Item"

    def __str__(self):
        print(self.name)

class NewsModel(models.Model):
    """ News Dataset Model """
    url = models.TextField(blank=True)
    title = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    date = models.TextField(blank=True)
    tags = models.TextField(blank=True)
    text = models.TextField(blank=True)
    code = models.TextField(blank=True)

    class Meta:
        verbose_name = "News Model"
