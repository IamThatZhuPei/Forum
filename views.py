# coding: utf-8
from django.shortcuts import render
from block.models import Block
from message.models import Message


def index(request):
    # block_infos = [{"name": "运维专区", "desc": "运维学习讨论区", "manager": "admin"},
    #                {"name": "Django专区", "desc": "Django学习讨论区", "manager": "admin"},
    #                {"name": "部落建设", "desc": "有关部落建设的事宜", "manager": "admin"}]
    # block_infos = Block.objects.all().order_by("-id")
    block_infos = Block.objects.filter(status=0).order_by("-id")
    msg_cnt = None
    if request.user.is_authenticated():
        msg_cnt = Message.objects.filter(owner=request.user, status=0).count()
    return render(request, 'index.html', {"blocks": block_infos, "msg_cnt": msg_cnt})
