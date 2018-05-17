# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission as AuthPermission
from permission.models import AssetPermission
from django.utils.encoding import force_text
from django.utils.translation import gettext as _


class GroupAddForm(forms.Form):
    name = forms.CharField(
        required = True,
        label = "用户组名称",
        error_messages = {'required': "请输入用户组名称"},
        max_length = 20,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'输入名称，必填项'}
        )
    )
    des = forms.CharField(
        required=True,
        label="用户组名称",
        error_messages={'required': "请输入用户组名称"},
        max_length=20,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'输入名称，必填项'}
        )
    )



#
# class CustomModelMultipleChoiceField(forms.ModelMultipleChoiceField):
#         def label_from_instance(self, obj):
#             return force_text(_(obj.name))


class PermissionForm(forms.ModelForm):

    # perm = CustomModelMultipleChoiceField(
    #     queryset = AuthPermission.objects.filter(
    #         content_type__app_label__in=['assets','navi','permission'],codename__contains='can_'
    #     ),
    #     # widget = forms.CheckboxSelectMultiple()
    # )

    class Meta:
        model = AssetPermission
        fields = ['group', 'assetsgroup',]
        widgets = {
            'group': forms.Select(attrs={'class': 'form-control'}),
            'assetsgroup': forms.SelectMultiple(attrs={'class': 'form-control', 'size': '10', 'multiple': 'multiple'}),
            # 'perm': forms.SelectMultiple(attrs={'class': 'form-control', 'size': '10', 'multiple': 'multiple'}),

        }

    def __init__(self, *args, **kwargs):
        super(PermissionForm, self).__init__(*args, **kwargs)
        self.fields['group'].label = u'用户组'
        self.fields['group'].error_messages = {'required': u'请选择用户组'}
        self.fields['assetsgroup'].label = u'资产组'
        self.fields['assetsgroup'].error_messages = {'required': u'请选择资产组'}

