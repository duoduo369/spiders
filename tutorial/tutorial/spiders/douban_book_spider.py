# -*- coding: utf-8 -*-

from os import linesep

from utils import cover_data
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from tutorial.items import BookItem

class GroupSpider(CrawlSpider):
    name = "douban_book"
    allowed_domains = ["douban.com"]
    start_urls = [
        #u'http://book.douban.com/tag/?view=type'
        u'http://book.douban.com/tag/小说'
    ]

    rules = [
        # 规则 获得页面里面的下一页，follow爬下去
        Rule(SgmlLinkExtractor(
                allow=('/subject/\d+/$',),
                restrict_xpaths=('//*[@id="subject_list"]/*',),
            ),
            callback='parse_book',
            process_request='add_cookie',
        ),
        # 规则 获得页面里面的下一页，follow爬下去
        Rule(SgmlLinkExtractor(
                allow=('/tag/[^/]+\?start=',),
                restrict_xpaths=('//*[@id="subject_list"]/'
                                 'div[@class="paginator"]/span[@class="next"]/a',),
            ),
            callback='parse_book_tag',
            follow=True,
            process_request='add_cookie',
        ),
    ]


    def add_cookie(self, request):
        request.replace(cookies=[
            {'name': 'COOKIE_NAME',
             'value': 'VALUE',
             'domain': '.book.douban.com',
             'path': '/'},
            ]);
        return request;

    def parse_book(self, response):
        sel = Selector(response)
        p_article = sel.css(".article")
        p_info = p_article.css("#info")
        fetch_dict = {
            u'</span>:\s*.*<a.*>(.*)</a>\s*</span>': {
                'author': u'作者',
                'translator': u'译者',
            },
            u':</span>\s*(.*?)元<br>': {
                'price': u'定价',
            },
            u':</span>\s*.*<a.*>(.*)</a>\s*<br>': {
                'series': u'丛书',
            },
            u':</span>\s*(.*?)<br>': {
                'pub': u'出版社',
                'origin_title': u'原作名',
                'pub_date': u'出版年',
                'pages': u'页数',
                'binding': u'装帧',
                'ISBN': u'ISBN'
            },
        }
        data = {
            'title': sel.css("#wrapper > h1 > span").xpath('text()'),
            'cover': p_article.xpath('//*[@id="mainpic"]/a/img/@src'),
            'link': response.url,
        }
        for _re, each in fetch_dict.iteritems():
            for key, word in each.iteritems():
                data[key] = p_info.re(word+_re)
        cover_data(data)
        item = BookItem()
        for attr, value in data.iteritems():
            item[attr] = value
        try:
            item['price'] = float(item['price'])
        except ValueError as ex:
            item['price'] = 0
            print ex
        return item

    def parse_book_tag(self, response):
        url = response.url
        self.log(url)
        with open('./data/book_tag', 'a') as f:
            f.write(url)
            f.write(linesep)
