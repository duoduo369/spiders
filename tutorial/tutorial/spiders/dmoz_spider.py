# -*- coding: utf-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector

from tutorial.items import DmozItem


class DmozSpider(Spider):
    name = 'dmoz'
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.css('ul li')
        items = []
        for site in sites:
            item = DmozItem()
            item['title'] = site.css('a::text').extract()
            item['link'] = site.css('a::attr(href)').extract()
            item['desc'] = site.css('::text').extract()
            items.append(item)
        return items
