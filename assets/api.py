# -*- coding:utf8 -*-
from rest_framework import viewsets, filters, permissions
# from .models import query_idc_by_args
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Idc, AssetGroup, Assets
from .serializers import IdcSerializer, AssetGroupSerializer, AssetsSerializer


class IdcViewSet(viewsets.ModelViewSet):
    """
    机房
    """
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer
    permission_classes = (permissions.IsAuthenticated,) # 权限检查，支持7种权限
    filter_backends = (filters.SearchFilter,)           # rest-framework 提供的默认的filters
    search_fields = ('name', 'address')                  # 指定搜索的域,http://example.com/api/idc/?search=Azure


class AssetGroupViewSet(viewsets.ModelViewSet):
    """
    主机资产组
    """
    queryset = AssetGroup.objects.all()
    serializer_class = AssetGroupSerializer
    permission_classes = (permissions.IsAuthenticated,) # 权限检查，支持7种权限
    filter_backends = (filters.SearchFilter,)           # rest-framework 提供的默认的filters
    search_fields = ('name', 'desc')                  # 指定搜索的域,http://example.com/api/idc/?search=Azure


class AssetViewSet(viewsets.ModelViewSet):
    """
    主机资产
    """
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('hostname','ip')
