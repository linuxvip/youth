#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    """admin界面的定义"""
    # list_display = ['username','password','group','memo']
    # filter_horizontal = ['name']


admin.site.register(UserProfile, UserProfileAdmin)