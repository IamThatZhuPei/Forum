# coding: utf-8
from django.shortcuts import render
from block.models import Block
from .models import Article
from django.core.paginator import Paginator
from utilFunc import paginate_queryset

__author__ = '朱沛'

ARTICLE_CNT_1PAGE = 3


def article_list(request, block_id):

    page_no = int(request.GET.get("page_no", "1"))

    block_id = int(block_id)
    # print(block_id)
    block = Block.objects.get(id=block_id)
    all_article_objs = Article.objects.filter(block=block, status=0).order_by("-id")

    # 分页代码段
    # p = Paginator(all_article_objs, ARTICLE_CNT_1PAGE)
    # page = p.page(page_no)
    # # article_objs = Article.objects.filter(block__id=block_id, status=0).order_by("-id")
    #
    # page_elem = dict()
    # page_elem["page_cnt"] = p.num_pages
    # page_elem["current_no"] = page_no
    # page_elem["page_links"] = [i for i in range(page_no - 5, page_no + 6) if 0 < i <= p.num_pages]
    # page_elem["previous_link"] = page_elem["page_links"][0] - 1
    # page_elem["next_link"] = page_elem["page_links"][-1] + 1
    # page_elem["has_previous"] = page_elem["previous_link"] > 0
    # page_elem["has_next"] = page_elem["next_link"] <= page_elem["page_cnt"]

    page_articles, pagination_data = paginate_queryset(all_article_objs, page_no)

    return render(request, "article_list.html", {"articles": page_articles, "b": block, "page_elem": pagination_data})

