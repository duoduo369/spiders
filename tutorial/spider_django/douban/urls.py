#coding: utf-8

from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^douban/books$', views.BookList.as_view()),
)

