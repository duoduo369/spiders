# -*- coding: utf-8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.contrib.djangoitem import DjangoItem
from douban.models import Book

class DmozItem(Item):
    title = Field()
    link = Field()
    desc = Field()

class BookItem(DjangoItem):
    django_model = Book
