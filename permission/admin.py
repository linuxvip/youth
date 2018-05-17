#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import AssetPermission

# Register your models here.


class AssetPermissionAdmin(admin.ModelAdmin):
    """admin界面的定义"""
    list_display = ['group',]
    # filter_horizontal = ['name']


admin.site.register(AssetPermission, AssetPermissionAdmin)
