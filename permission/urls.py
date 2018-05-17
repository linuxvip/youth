#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url

from permission.views import (PermissionListView,
                              PermissionAddView,
                              PermissionEditView,
                              PermissionDeleteView,
                              )

# UserUpdate,PermissionUpdate,

urlpatterns = [
    # 权限相关
    url(r'^permission/list/$',PermissionListView.as_view(),name='permission-list'),
    url(r'^permission/add/$', PermissionAddView.as_view(), name='permission-add'),
    url(r'^permission/(?P<pk>[0-9]+)/edit/$',PermissionEditView.as_view(),name='permission-edit'),
    url(r'^permission/(?P<pk>[0-9]+)/delete/$',PermissionDeleteView.as_view(),name='permission-delete'),
]