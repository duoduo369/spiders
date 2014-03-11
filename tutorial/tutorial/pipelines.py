# -*- coding: utf-8 -*-
import json
from scrapy.contrib.djangoitem import DjangoItem

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('./data/douban/book.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

class DjangoPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item, DjangoItem):
            item.save()
        return item
