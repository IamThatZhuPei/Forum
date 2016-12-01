# coding: utf-8
from django.db import models
from django.contrib.auth.models import User

__author__ = '朱沛'


class ActivateCode(models.Model):
    user = models.ForeignKey(User, verbose_name="用户")
    activate_code = models.CharField("激活码", max_length=50, null=False)
    expiration_time = models.DateTimeField("过期时间")

    def __str__(self):
        return self.activate_code

    class Meta:
        verbose_name = "用户激活码"
        verbose_name_plural = "用户激活码"