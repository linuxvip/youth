#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Idc, AssetGroup, Assets

# Register your models here.


class IdcAdmin(admin.ModelAdmin):
    """admin界面的定义"""
    list_display = ['name','address','tel','contact']
    # filter_horizontal = ['name']


class AssetGroupsAdmin(admin.ModelAdmin):
    list_display = ['name','desc']


class AssetsAdmin(admin.ModelAdmin):
    readonly_fields = ('add_time', 'update_time',)
    list_display = ['hostname','ip','asset_type','status','group','idc']

admin.site.register(Idc, IdcAdmin)
admin.site.register(AssetGroup, AssetGroupsAdmin)
admin.site.register(Assets, AssetsAdmin)
admin.site.site_header = 'CMDB资产管理系统' # 此处设置页面显示标题
# admin.site.site_title = 'CMDB资产管理系统' # 此处设置页面头部标题