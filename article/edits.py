# coding: utf-8
from django.shortcuts import render, redirect
from block.models import Block
from .models import Article
from .forms import ArticleForm
from django.views.generic import View, DetailView


# __author__ = '朱沛'


# def create_article(request, block_id):
#     block_id = int(block_id)
#     block = Block.objects.get(id=block_id)
#     if request.method == "GET":
#         return render(request, "create_article.html", {"b": block})
#     else:
#         form = ArticleForm(request.POST)
#         # title = request.POST["title"].strip()
#         # content = request.POST["content"].strip()
#         # if not title or not content:
#         #     return render(request, "create_article.html",
#         #                   {"b": block, "error": "标题和内容都不能为空", "title": title, "content": content})
#         # if len(title) > 100 or len(content) > 10000 :
#         #     return render(request, "create_article.html",
#         #                   {"b": block, "error": "标题或内容太长了", "title": title, "content": content})
#         # article = Article(block=block, title=title, content=content, status=0)
#         # article.save()
#         # return redirect("/article/list/%s" % block_id)
#         if form.is_valid():
#             # article = Article(block=block, title=form.cleaned_data["title"],
#             #                   content=form.cleaned_data["content"], status=0)
#             article = form.save(commit=False)
#             article.block = block
#             article.status = 0
#             article.save()
#             return redirect("/article/list/%s" % block_id)
#         else:
#             return render(request, "create_article.html", {"b": block, "form": form})


class ArticleCreateView(View):

    template_name = "create_article.html"

    def init_data(self, block_id):
        self.block_id = block_id
        self.block = Block.objects.get(id=block_id)

    def get(self, request, block_id):
        self.init_data(block_id)
        return render(request, self.template_name, {"b": self.block})

    def post(self, request, block_id):
        self.init_data(block_id)
        if request.user.is_authenticated():
            form = ArticleForm(request.POST)
            user = request.user
            if form.is_valid():
                article = form.save(commit=False)
                article.owner = user
                article.block = self.block
                article.status = 0
                article.save()
                return redirect("/article/list/%s" % block_id)
            else:
                return render(request, self.template_name, {"b": self.block, "form": form})
        else:
            return redirect("/accounts/login")


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'a'
