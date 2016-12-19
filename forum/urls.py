"""forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from comment.view import create_comment

import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^article/', include('article.urls')),
    url(r'^user/', include('usermodulo.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^comment/create/', create_comment),
    url(r'^message/', include('comment.urls')),
    url(r'^ueditor/', include('DjangoUeditor.urls')),

    # url(r'^static/(?P<path>.*)$', django.contrib.staticfiles.views.serve), #django 内置静态文件处理
]
