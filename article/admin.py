# coding: utf-8
from django.contrib import admin
from .models import Article

__author__ = '朱沛'


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("block", "title", "content", "status", "create_timestamp", "last_update_timestamp")  # 元祖


admin.site.register(Article, ArticleAdmin)
