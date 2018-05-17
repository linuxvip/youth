#! /usr/bin/env python
# -*- coding: utf-8 -*-
""" URL Configuration

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
from django.views.generic.base import RedirectView

from assets.urls import router as assets_router
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

schema_view = get_schema_view(title="CMDB API")


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='/navi'), name='index'),
    url(r'^user/', include('users.urls', namespace='user')),
    url(r'^navi/', include('navi.urls', namespace='navi')),
    url(r'^permission/', include('permission.urls', namespace='permission')),
    url(r'^asset/', include('assets.urls', namespace='assets')),
    url(r'^domain/', include('domain.urls', namespace='domain')),

    # 资产API
    url(r'^api/', include(assets_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^docs/', include_docs_urls(title="CMDB Api Docs")),
    url('^schema/$', schema_view),
]
