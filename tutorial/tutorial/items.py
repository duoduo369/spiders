# -*- coding: utf-8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class DmozItem(Item):
    title = Field()
    link = Field()
    desc = Field()

class BookItem(Item):
    title = Field()
    # info.re(u'作者</span>:\s*.*\s*</span>')
    author = Field()
    pub = Field()
    origin_title = Field()
    translator = Field()
    pub_date = Field()
    pages = Field()
    price = Field()
    binding = Field()
    series = Field()
    ISBN = Field()
    link = Field()
    desc = Field()
    rate = Field()
    tags = Field()
    rate_peoples = Field()
    star_1 = Field()
    star_2 = Field()
    star_3 = Field()
    star_4 = Field()
    star_5 = Field()

class BookTag(Item):
    tag = Field()
