# coding: utf-8
from django import forms
from .models import Article

__author__ = '朱沛'


class ArticleForm(forms.ModelForm):
    # title = forms.CharField(label="标题", max_length=100)
    # content = forms.CharField(label="内容", max_length=10000)
    class Meta:
        model = Article
        fields = ['title', 'content']
