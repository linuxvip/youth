#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url

from views import (
    DomainListView,
    DomainDeleteView,
    DomainAddView,
    DomainEditView,
)


urlpatterns = [
    # url(r'^test/$', TestView.as_view(), name='domain-test'),
    url(r'^list/$', DomainListView.as_view(), name='domain-list'),
    url(r'^add/$', DomainAddView.as_view(), name='domain-add'),
    url(r'^delete/(?P<pk>\d+)/$', DomainDeleteView.as_view(), name='domain-delete'),
    url(r'^edit/(?P<pk>\d+)/$', DomainEditView.as_view(), name='domain-edit'),
]
