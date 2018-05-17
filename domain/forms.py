#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.forms.widgets import *

from .models import Domain


class DomainForm(forms.ModelForm):

    class Meta:
        model = Domain
        exclude = ("id","add_time","expiration_time")

        widgets = {
            'domain_name': TextInput(attrs={'class': 'form-control','style': 'width:450px;', 'placeholder': u'域名名称，必填项'}),
            'ip': TextInput(attrs={'class': 'form-control','style': 'width:450px;', 'placeholder': u'解析IP，必填项'}),
            'env': TextInput(attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'使用环境，可选填'}),
            'add_area': Select(attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'添加位置'}),
            'usage': TextInput(attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'用途，必填项'}),
            'applicant': TextInput(attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'申请人，必填项'}),
        }