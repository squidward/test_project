# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('myproject.myapp.views',
    url(r'^list/$', 'list', name='list'),
    url(r'^list2/$', 'show', name='list2'),
    url(r'^mytext/$', 'mytext', name='mytext'),
    url(r'^redtext/$', 'redactortext', name='redtext'),
)
