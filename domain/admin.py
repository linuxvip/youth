#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Domain

# Register your models here.


class DomainAdmin(admin.ModelAdmin):
    """admin界面的定义"""
    list_display = ['domain_name','ip','env','add_area','usage','applicant',]


admin.site.register(Domain, DomainAdmin)