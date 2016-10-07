# coding: utf-8
from django.shortcuts import render, redirect
from block.models import Block
from .models import Article


# __author__ = '朱沛'


def create_article(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    if request.method == "GET":
        return render(request, "create_article.html", {"b": block})
    else:
        title = request.POST["title"].strip()
        content = request.POST["content"].strip()
        if not title or not content:
            return render(request, "create_article.html",
                          {"b": block, "error": "标题和内容都不能为空", "title": title, "content": content})
        if len(title) > 100 or len(content) > 10000 :
            return render(request, "create_article.html",
                          {"b": block, "error": "标题或内容太长了", "title": title, "content": content})
        article = Article(block=block, title=title, content=content, status=0)
        article.save()
        return redirect("/article/list/%s" % block_id)
