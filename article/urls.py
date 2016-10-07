# coding: utf-8
from django.conf.urls import url
from .views import article_list
from .edits import create_article

__author__ = '朱沛'

urlpatterns = [
    url(r'list/(?P<block_id>\d+)', article_list),
    url(r'create/(?P<block_id>\d+)', create_article),
]
