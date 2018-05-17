#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter


from assets import views
from assets import api


router = DefaultRouter()
router.register(r'idcs', api.IdcViewSet)
router.register(r'assetgroups', api.AssetGroupViewSet)
router.register(r'assets', api.AssetViewSet)

urlpatterns = [
    # Asset
    url(r'^host/list/$', views.AssetListView.as_view(), name='asset-list'),
    url(r'^host/add/$', views.AssetAddView.as_view(), name='asset-add'),
    url(r'^host/delete/(?P<pk>\d+)/$', views.AssetDeleteView.as_view(), name='asset-delete'),
    url(r'^host/edit/(?P<pk>\d+)/$', views.AssetEditView.as_view(), name='asset-edit'),

    # IDC
    url(r'^idc/list/$', views.IdcListView.as_view(), name='idc-list'),
    url(r'^idc/add/', views.IdcAddView.as_view(), name='idc-add'),
    url(r'^idc/delete/(?P<pk>\d+)/$', views.IdcDeleteView.as_view(), name='idc-delete'),
    url(r'^idc/edit/(?P<pk>\d+)/$', views.IdcEditView.as_view(), name='idc-edit'),

    # AssetGroup
    url(r'^group/list/$', views.AssetGroupListView.as_view(), name='asset-group-list'),
    url(r'^group/add/', views.AssetGroupAddView.as_view(), name='asset-group-add'),
    url(r'^group/delete/(?P<pk>\d+)/$', views.AssetGroupDeleteView.as_view(), name='asset-group-delete'),
    url(r'^group/edit/(?P<pk>\d+)/$', views.AssetGroupEditView.as_view(), name='asset-group-edit'),

    # Api信息

]