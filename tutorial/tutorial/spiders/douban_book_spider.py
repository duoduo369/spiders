# -*- coding: utf-8 -*-

from os import linesep
from operator import itemgetter

from utils import cover_data
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from tutorial.items import BookItem
from douban.models import Book

class GroupSpider(CrawlSpider):
    name = "douban_book"
    allowed_domains = ["douban.com"]
    start_urls = [
        # u'http://book.douban.com/tag/?view=type'
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
        ])
        return request

    def parse_book(self, response):
        if Book.objects.filter(link=response.url).first():
            return None
        sel = Selector(response)
        get_0 = itemgetter(0)
        p_article = sel.css('.article')
        p_info = p_article.css('#info')
        p_interest_sectl = p_article.css('#interest_sectl')
        p_intro = p_article.css('#link-report .intro')
        _desc = [p.xpath('text()').extract() for p in p_intro.css('p')]
        desc = linesep.join(get_0(text_list) for text_list in _desc if text_list)
        rate_stars = p_interest_sectl.re('</div>\s*(\d+\.\d+)')
        fetch_dict = {
            u'</span>:\s*.*<a.*>(.*)</a>\s*</span>': {
                'author': u'作者',
                'translator': u'译者',
            },
            u':</span>\s*(.*?)元*<br>': {
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
            'desc': desc,
            'rate': p_interest_sectl.css('.rating_num').xpath("text()").re('\d\.\d'),
            'rate_peoples': p_interest_sectl.css('[href=collections]>span').xpath("text()"),
        }
        for index, percent in enumerate(rate_stars):
            data['star_'+str(index+1)] = percent

        for _re, each in fetch_dict.iteritems():
            for key, word in each.iteritems():
                data[key] = p_info.re(word + _re)
        cover_data(data)
        item = BookItem()
        for attr, value in data.iteritems():
            item[attr] = value
        float_attr = ['price', 'rate', 'star_1', 'star_2', 'star_3', 'star_4', 'star_5']
        int_attr = ['pages', 'rate_peoples']
        for attr in int_attr:
            try:
                int(item[attr])
            except ValueError as ex:
                print '================'
                print attr, item[attr]
                del item[atrr]
                print ex

        for attr in float_attr:
            try:
                float(item[attr])
            except ValueError as ex:
                print '================'
                print attr, item[attr]
                del item[attr]
                print ex
        return item

    def parse_book_tag(self, response):
        url = response.url
        self.log(url)
        with open('./data/book_tag', 'a') as f:
            f.write(url)
            f.write(linesep)
