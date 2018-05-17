#! /usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import viewsets, filters, permissions
from serializers import NAVISerializer
from models import NAVI


class NAVIViewSet(viewsets.ModelViewSet):
    queryset = NAVI.objects.all()
    serializer_class = NAVISerializer
    # permission_classes = (permissions.IsAuthenticated,)  # 权限检查，支持7种权限
    filter_backends = (filters.SearchFilter,)              # rest-framework 提供的默认的filters
    search_fields = ('name','url')                         # 指定搜索的域,http://example.com/api/idc/?search=Azure