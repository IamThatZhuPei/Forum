# coding: utf-8
from django.shortcuts import render, redirect
from article.models import Article
from .models import Comment
from utilFunc import json_response
from django.contrib.auth.models import User
from message.models import Message
from django.http import HttpResponseRedirect


def create_comment(request):
    # if request.method == "POST":
        if request.user.is_authenticated():
            owner = request.user
            article_id = request.POST.get("article_id")
            to_comment_id = int(request.POST.get("to_comment_id", 0))

            content = request.POST.get("content")
            article = Article.objects.get(id=article_id)
            try:
                if to_comment_id != 0:
                    to_comment = Comment.objects.get(id=to_comment_id)
                    link = "/article/detail/" + article_id + "?page_no=1000"
                    create_message(to_comment.owner, link, to_comment.content)
                    # owner = owner
                    # content = r"有人回复了你的评论：‘" + comment + "’"
                    # message = Message(owner=to_comment.owner, content=to_comment.content, link=link)
                    # message.save()

                else:
                    to_comment = None
                comment = Comment(content=content, article=article,
                                  owner=owner, to_comment=to_comment)
                comment.save()
                msg = {"status": "ok", "msg": ""}
                return json_response(msg)
            except Exception as e:
                msg = {"status": "err", "msg": e}
                return json_response(msg)

        else:

            msg = {"status": "err", "msg": "请登录"}
            return json_response(msg)


def create_message(owner, link, comment):
    owner = owner
    content = r"有人回复了你的评论：‘" + comment + "’"
    message = Message(owner=owner, content=content, link=link)
    message.save()


def message_list(request):
    all_message = None
    if request.method == "GET":
        if request.user.is_authenticated():
            owner = request.user
            all_message = Message.objects.filter(owner=owner).order_by("-create_time")

    return render(request, "message_list.html", {"msgs": all_message})


def message_read(request, msg_id):
    if request.method == "GET":
        message = Message.objects.get(id=msg_id)
        message.status = 1
        message.save()

        print("abccccc", message.link)

        return HttpResponseRedirect(message.link)
