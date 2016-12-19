# coding: utf-8
from django.conf.urls import url
from .view import message_list, message_read
__author__ = '朱沛'

urlpatterns = [
    url(r'list/', message_list),
    url(r'read/(?P<msg_id>\d+)', message_read),
]