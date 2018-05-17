#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.forms.widgets import *

from .models import Assets, Idc, AssetGroup


class AssetForm(forms.ModelForm):

    class Meta:
        model = Assets
        exclude = ("id","add_time","update_time",)

        widgets = {
            'hostname': TextInput(attrs={'class': 'form-control','style': 'width:450px;', 'placeholder': u'主机名称，必填项'}),
            'ip': TextInput(attrs={'class': 'form-control','style': 'width:450px;', 'placeholder': u'IP地址，必填项 例如：8.8.8.8'}),
            'other_ip': TextInput(attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'外网IP，可选填'}),
            'asset_type': Select(attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'设备类型，可选填'}),
            'status': Select(attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'设备状态，可选填'}),
            'os': TextInput(attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'操作系统，可选填'}),
            'cpu_num': NumberInput(attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'CPU数量，可选填'}),
            'memory': TextInput(attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'内存大小，可选填'}),
            'disk': TextInput(attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'硬盘信息，可选填'}),
            'sn': TextInput(attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'SN号码，可选填'}),
            'usage': TextInput(attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'机器用途，可选填'}),
            'application': TextInput(attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'装机软件，可选填'}),
            'principal': TextInput(attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'负责人，可选填'}),
            'memo': TextInput(attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'备注信息，可选填'}),
            'jira': TextInput(attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'申请jira，可选填'}),
            'group': Select(attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'资产组，可选填'}),
            'idc': Select(attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'所在机房，可选填'}),
        }


class IdcForm(forms.ModelForm):

    class Meta:
        model = Idc
        exclude = ("id",)

        widgets = {
            'name': TextInput(attrs={'class': 'form-control','style': 'width:450px;', 'placeholder': u'机房名称，必填项'}),
            'address': TextInput(attrs={'class': 'form-control','style': 'width:450px;', 'placeholder': u'机房地址，可选填'}),
            'tel': TextInput(attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'机房电话，可选填'}),
            'contact': TextInput(attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'客户经理，可选填'}),
        }


class AssetGroupForm(forms.ModelForm):

    class Meta:
        model = AssetGroup
        exclude = ("id",)

        widgets = {
            'name': TextInput(attrs={'class': 'form-control','style': 'width:450px;', 'placeholder': u'主机组名称，必填项'}),
            'desc': TextInput(attrs={'class': 'form-control','style': 'width:450px;', 'placeholder': u'主机组描述，可选填'}),
        }