# coding: utf-8
from django.conf.urls import url
from .views import article_list
# from .edits import create_article
from .edits import ArticleCreateView, ArticleDetailView
from django.contrib.auth.decorators import login_required

__author__ = '朱沛'

urlpatterns = [
    url(r'list/(?P<block_id>\d+)', article_list),
    url(r'create/(?P<block_id>\d+)', login_required(ArticleCreateView.as_view())),
    url(r'detail/(?P<pk>\d+)', ArticleDetailView.as_view()),
]
