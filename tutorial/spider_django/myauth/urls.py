# -*- coding: utf-8 -*-
import views
import sina

from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^oauth2/sina/authorize$', sina.authorize),
    url(r'^$', views.index),
)
