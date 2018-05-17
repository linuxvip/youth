#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import NAVI

# Register your models here.


class NAVIAdmin(admin.ModelAdmin):
    """admin界面的定义"""
    list_display = ['name','description','url','memo']
    # filter_horizontal = ['name']


admin.site.register(NAVI, NAVIAdmin)