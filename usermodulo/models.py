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


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.IntegerField("性别", choices=((0, '男'), (-1, '女')), default=0)
    birthday = models.DateTimeField("生日", null=True, blank=True)
    avatar = models.CharField("头像", max_length=300, blank=True)

    # 面包屑 显示内容
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = '用户属性'  # 说明时的名称
        verbose_name_plural = "用户属性"  # 列表中的名称

