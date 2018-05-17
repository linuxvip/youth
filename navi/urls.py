#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url

from views import NaviListView, NaviManageView, NaviAddView, NaviDeleteView, NaviEditView
from navi import views

# NAVI API
from rest_framework import routers
from api import NAVIViewSet

# Register NAVI API
router = routers.DefaultRouter()
router.register(r'navi', NAVIViewSet)


urlpatterns = [
    url(r'^$', NaviListView.as_view(), name='navi-index'),
    url(r'^manage/', NaviManageView.as_view(), name='navi-manage'),
    url(r'^add/', NaviAddView.as_view(), name='navi-add'),
    url(r'^delete/(?P<pk>\d+)/$', NaviDeleteView.as_view(), name='navi-delete'),
    url(r'^edit/(?P<pk>\d+)/$', NaviEditView.as_view(), name='navi-edit'),
]
