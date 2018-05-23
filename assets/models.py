#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import django.utils.timezone as timezone
from django.db.models import Q
from django.db import models


ASSET_STATUS = (
    (str(1), u"使用中"),
    (str(2), u"未使用"),
    (str(3), u"故障"),
    (str(4), u"其它"),
    )

ASSET_TYPE = (
    (str(1), u"物理机"),
    (str(2), u"虚拟机"),
    (str(3), u"容器"),
    (str(4), u"网络设备"),
    (str(5), u"其他")
    )


class Idc(models.Model):
    name = models.CharField(u"机房名称", max_length=30, null=True)
    address = models.CharField(u"机房地址", max_length=100, null=True)
    tel = models.CharField(u"机房电话", max_length=30, null=True)
    contact = models.CharField(u"客户经理", max_length=30, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'机房'
        verbose_name_plural = verbose_name
        db_table = 'idc'

        permissions = (
            ("can_add_idc", "添加机房"),
            ("can_change_idc", "修改机房"),
            ("can_delete_idc", "删除机房"),
            ("can_view_idc", "查看机房"),
        )


class AssetGroup(models.Model):
    name = models.CharField(u"资产组名称", max_length=30, unique=True)
    desc = models.CharField(u"描述信息", max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "资产组"
        verbose_name_plural = verbose_name
        db_table = 'assetgroup'

        permissions = (
            ("can_add_assetgroup", "添加资产组"),
            ("can_change_assetgroup", "修改资产组"),
            ("can_delete_assetgroup", "删除资产组"),
            ("can_view_assetgroup", "查看资产组"),
        )


class Assets(models.Model):
    hostname = models.CharField(u"主机名", max_length=50)
    ip = models.GenericIPAddressField(u"管理IP", max_length=15)
    other_ip = models.CharField(u"其它IP", max_length=100, null=True, blank=True)
    group = models.ForeignKey(AssetGroup, verbose_name=u"资产组", on_delete=models.SET_NULL, null=True, blank=True)
    idc = models.ForeignKey(Idc, verbose_name=u"所在机房", on_delete=models.SET_NULL, null=True, blank=True)
    asset_type = models.CharField(u"设备类型", choices=ASSET_TYPE, max_length=30, null=True, blank=True)
    status = models.CharField(u"设备状态", choices=ASSET_STATUS, max_length=30, null=True, blank=True)
    os = models.CharField(u"操作系统", max_length=100, null=True, blank=True)
    cpu_num = models.CharField(u"CPU数量", max_length=100, null=True, blank=True)
    memory = models.CharField(u"内存大小", max_length=30, null=True, blank=True)
    disk = models.CharField(u"硬盘信息", max_length=255, null=True, blank=True)
    sn = models.CharField(u"SN号码", max_length=60, unique=True)
    usage = models.CharField(u"用途", max_length=100, null=True, blank=True)
    application = models.CharField(u"软件", max_length=100, null=True, blank=True)
    principal = models.CharField(u"负责人", max_length=50, null=True, blank=True)
    memo = models.TextField(u"备注信息", max_length=200, null=True, blank=True)
    jira = models.CharField(u"申请jira", max_length=200, null=True, blank=True)
    # add_time = models.DateTimeField(u"添加时间", auto_now_add=True)
    # update_time = models.DateTimeField(u"更新时间", auto_created=True, auto_now=True)
    add_time = models.DateTimeField(u"添加时间", default = timezone.now)
    update_time = models.DateTimeField(u"更新时间", auto_created=True, auto_now=True)

    def __unicode__(self):
        return self.hostname

    class Meta:
        verbose_name = "资产信息"
        verbose_name_plural = verbose_name
        db_table = 'assets'

        permissions = (
            ("can_add_asset", "添加资产"),
            ("can_change_asset", "修改资产"),
            ("can_delete_asset", "删除资产"),
            ("can_view_asset", "查看资产"),
        )