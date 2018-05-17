#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url

from views import LoginView, LogoutView, UserListView, UserAddView, UserDeleteView, GroupListView


urlpatterns = [
    # 用户相关
    url(r'login/$',LoginView.as_view(), name='login'),
    url(r'logout/$', LogoutView.as_view(), name='logout'),

    url(r'^user/add/$', UserAddView.as_view(), name='user-add'),
    # url(r'^user/edit/(?P<pk>[0-9]+)/$',UserEditView.as_view(),name='user-edit'),
    url(r'^user/delete/(?P<pk>\d+)/$', UserDeleteView.as_view(), name='user-delete'),
    url(r'^user/list/$',UserListView.as_view(),name='user-list'),

    # 用户组相关
    # url(r'^group/add/$', UserAddView.as_view(), name='group-add'),
    # # url(r'^group/(?P<pk>[0-9]+)/update/$',UserUpdate.as_view(),name='group-update'),
    # url(r'^group/delete/(?P<pk>\d+)/$', UserDeleteView.as_view(), name='group-delete'),
    url(r'^group/list/$',GroupListView.as_view(),name='group-list'),
]
