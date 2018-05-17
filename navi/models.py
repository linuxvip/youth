#! /usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from django.db import models


class NAVI(models.Model):
    name = models.CharField(u"名称", max_length=50)
    url = models.URLField(u"网址")
    description = models.CharField(u"描述", max_length=50,null=True,blank=True)
    memo = models.TextField(u"备注信息", max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "站点导航"
        verbose_name_plural = verbose_name
        db_table = 'navi'

        permissions = (
            ("can_add_navi", "添加站点"),
            ("can_change_navi", "修改站点"),
            ("can_delete_navi", "删除站点"),
            ("can_view_navi", "查看站点"),
        )