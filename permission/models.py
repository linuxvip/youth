# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from assets.models import AssetGroup
from django.contrib.auth.models import User, Group
from django.contrib.auth.models import Permission as AuthPermission


class AssetPermission(models.Model):
    # user = models.OneToOneField(User, verbose_name="用户", default="")
    group = models.OneToOneField(Group, verbose_name="用户组", default="")
    # perm = models.ManyToManyField(AuthPermission, verbose_name="权限")
    assetsgroup = models.ManyToManyField(AssetGroup, verbose_name="资产组")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_created=True, auto_now=True, verbose_name="更新时间")
    memo = models.TextField(verbose_name=u"备注信息", blank=True)

    def __unicode__(self):
        return str(self.assetsgroup)

    class Meta:
        verbose_name = "权限信息"
        verbose_name_plural = verbose_name
        db_table = 'asset_permission'

        permissions = (
            ("can_add_asset_permission", "添加资产组权限"),
            ("can_change_asset_permission", "修改资产组权限"),
            ("can_delete_asset_permission", "删除资产组权限"),
            ("can_view_asset_permission", "查看资产组权限"),
        )