# coding: utf-8
from django.contrib import admin
from .models import ActivateCode

__author__ = '朱沛'


class ActivateCodeAdmin(admin.ModelAdmin):
    list_display = ("user", "activate_code", "expiration_time")  # 元祖


admin.site.register(ActivateCode, ActivateCodeAdmin)

