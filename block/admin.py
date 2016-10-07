# coding: utf-8
from django.contrib import admin
from .models import Block

__author__ = '朱沛'


class BlockAdmin(admin.ModelAdmin):
    list_display = ("name", "desc", "manager_name")  # 元祖


admin.site.register(Block, BlockAdmin)
