# -*- coding: utf-8 -*-
from scrapy.selector.unified import SelectorList

def cover_data(data):
    for key, value in data.iteritems():
        if isinstance(value, SelectorList):
            try:
                coverd = value.extract()[0]
            except IndexError as ex:
                print ex
                coverd = None

        elif isinstance(value, list):
            try:
                coverd = value[0]
            except IndexError as ex:
                print ex
                coverd = None
        elif isinstance(value, basestring):
            coverd = value
        else:
            print value, type(value)
            raise
        data[key] = coverd
    return data
