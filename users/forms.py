# -*- coding: utf-8 -*-

from django import forms
# from django.contrib.auth.models import User
from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)


class UserAddForm(forms.Form):
    user = forms.CharField(
            required = True,
            label = u"用户名",
            error_messages = {'required': "请输入一个有效的用户"},
            max_length = 20,
            widget=forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'输入用户，必填项'}
            )
    )
    newpassword1 = forms.CharField(
            required = True,
            label = u"输入密码",
            error_messages = {'required': "请输入你的密码"},
            widget = forms.PasswordInput(
                attrs = {'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'输入密码，必填项'}
            )
        )
    newpassword2 = forms.CharField(
            required = True,
            label = u"再次输入密码",
            error_messages = {'required': "请再次输入你的密码"},
            widget = forms.PasswordInput(
                attrs = {'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'确认密码，必填项'}
            )
        )
    email = forms.EmailField(
            required = True,
            label= u"邮箱",
            error_messages = {'required': "请输入有效的邮箱账号"},
            widget = forms.EmailInput(
            attrs = {'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'注册邮箱，必填项'}
            )
        )
    mobile = forms.CharField(
        required = False,
        label = u"手机号码",
        error_messages={'required': "请输入手机号码"},
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'width:450px;', 'placeholder': u'手机号码，非必填项'}
        )
    )

    def clean(self):

        if self.cleaned_data['newpassword1'] != self.cleaned_data['newpassword2']:
            raise forms.ValidationError({
                # 'newpassword1':u"俩次密码输入不一致",
                 'newpassword2':u"俩次密码输入不一致"
            })
        elif self.cleaned_data['user']:
            if UserProfile.objects.filter(username = unicode(self.cleaned_data['user'])):
                raise forms.ValidationError({
                    'user':u"用户名已经注册！"
                })
        cleaned_data = super(UserAddForm, self).clean()
        return cleaned_data
