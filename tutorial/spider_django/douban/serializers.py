#coding: utf-8

from rest_framework import serializers
from douban.models import Book

class BookSeri(serializers.ModelSerializer):

    class Meta:
        model = Book
