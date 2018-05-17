#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.forms.widgets import *

from .models import NAVI


class NaviForm(forms.ModelForm):

    # def clean(self):
    #     cleaned_data = super(IdcForm, self).clean()
    #     value = cleaned_data.get('name')
    #     try:
    #         Idc.objects.get(name=value)
    #         self._errors['name'] = self.error_class(["%s的信息已经存在" % value])
    #     except Idc.DoesNotExist:
    #         pass
    #     return cleaned_data

    class Meta:
        model = NAVI
        exclude = ("id",)

        widgets = {
            'name': TextInput(attrs={'class': 'form-control','style': 'width:450px;', 'placeholder': u'名称，必填项'}),
            'url': URLInput(attrs={'class': 'form-control','style': 'width:450px;', 'placeholder': u'url地址，必填项 例如：http://www.baidu.com/'}),
            'description': TextInput(attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'描述，可选填'}),
            'memo': TextInput(attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'备注，可选填'}),
        }
