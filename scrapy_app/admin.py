from django.contrib import admin
from .models import NewsData, NewsModel

class ScrapyAppAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'date', 'tags', 'code', 'text')
    list_display_links = ('url',)
    search_fields = ('tags', 'code')
    list_per_page = 10

class NewsModelRegAdmin(admin.ModelAdmin):
        list_display = ('url', 'title', 'date', 'tags', 'code')
        list_display_links = ('url',)
        search_fields = ('tags', 'code')
        list_per_page = 10

admin.site.register(NewsData, ScrapyAppAdmin)
admin.site.register(NewsModel, NewsModelRegAdmin)
