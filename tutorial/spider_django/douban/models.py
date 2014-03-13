# -*- coding: utf-8 -*-
from django.db import models
import model_settings as config

MAX_LENGTH_20 = config.MAX_LENGTH_20
MAX_LENGTH_200 = config.MAX_LENGTH_200
MAX_LENGTH_1024 = config.MAX_LENGTH_1024

class Book(models.Model):
    title = models.CharField(
        max_length=MAX_LENGTH_200,
        blank=True,
        null=True,
    )
    author = models.CharField(
        max_length=MAX_LENGTH_200,
        blank=True,
        null=True,
    )
    author_country = models.CharField(
        max_length=MAX_LENGTH_20,
        blank=True,
        null=True,
    )
    pub = models.CharField(
        max_length=MAX_LENGTH_200,
        blank=True,
        null=True,
    )
    origin_title = models.CharField(
        max_length=MAX_LENGTH_200,
        blank=True,
        null=True,
    )
    translator = models.CharField(
        max_length=MAX_LENGTH_200,
        blank=True,
        null=True,
    )
    cover = models.URLField(
        verbose_name=u'封面',
        blank=True,
        null=True,
    )
    pub_date = models.DateField(
        verbose_name=u'出版日期',
        blank=True,
        null=True,
    )
    pages = models.IntegerField(
        verbose_name=u'页数',
        blank=True,
        null=True,
    )
    price = models.FloatField(
        verbose_name=u'完成率',
        blank=True,
        null=True,
    )
    binding = models.CharField(
        verbose_name=u'装帧',
        max_length=MAX_LENGTH_20,
        blank=True,
        null=True,
    )
    series = models.CharField(
        verbose_name=u'丛书',
        max_length=MAX_LENGTH_200,
        blank=True,
        null=True,
    )
    ISBN = models.CharField(
        max_length=MAX_LENGTH_20,
        blank=True,
        null=True,
    )
    link = models.URLField(
        verbose_name=u'url',
        blank=True,
        null=True,
    )
    desc = models.TextField(
        verbose_name=u'描述',
        blank=True,
        null=True,
    )
    rate = models.FloatField(
        verbose_name=u'评分',
        blank=True,
        null=True,
    )
    tags = models.CharField(
        verbose_name=u'标签',
        max_length=MAX_LENGTH_1024,
        blank=True,
        null=True,
    )
    rate_peoples = models.BigIntegerField(
        verbose_name=u'评论人数',
        max_length=30,
        default=0,
    )
    star_1 = models.FloatField(
        verbose_name=u'1星',
        blank=True,
        null=True,
    )
    star_2 = models.FloatField(
        verbose_name=u'2星',
        blank=True,
        null=True,
    )
    star_3 = models.FloatField(
        verbose_name=u'3星',
        blank=True,
        null=True,
    )
    star_4 = models.FloatField(
        verbose_name=u'4星',
        blank=True,
        null=True,
    )
    star_5 = models.FloatField(
        verbose_name=u'5星',
        blank=True,
        null=True,
    )
