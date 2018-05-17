#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=20, verbose_name=u"昵称", default="")
    mobile = models.CharField(max_length=11, verbose_name=u"手机号码", null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
        db_table = "users"

    def __unicode__(self):
        return self.username

    permissions = (
        ("can_add_user", "添加用户"),
        ("can_change_user", "修改用户"),
        ("can_delete_user", "删除用户"),
        ("can_view_user", "查看用户"),

        ("can_add_group", "添加用户组"),
        ("can_change_group", "修改用户组"),
        ("can_delete_group", "删除用户组"),
        ("can_view_group", "查看用户组"),
    )