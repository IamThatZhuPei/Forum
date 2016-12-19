# coding: utf-8
from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    owner = models.ForeignKey(User, verbose_name="作者")
    content = models.CharField("消息内容", max_length=200)
    link = models.CharField("消息目标链接", max_length=200)
    status = models.IntegerField("状态", choices=((0, "未读"), (1, "已读")), default=0)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("最近阅读时间", auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "消息"
        verbose_name_plural = "消息1"
