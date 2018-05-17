#! /usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Idc, AssetGroup, Assets


class IdcSerializer(serializers.ModelSerializer):
    """
       继承serializers.ModelSerializer
       fields为API想要得到的字段。
    """
    class Meta:
        model = Idc
        fields = (
            'id',
            'name',
            'address',
            'tel',
            'contact',
        )


class AssetGroupSerializer(serializers.ModelSerializer):
    """
       继承serializers.ModelSerializer
       fields为API想要得到的字段。
    """

    class Meta:
        model = AssetGroup
        fields = (
            'id',
            'name',
            'desc',
        )


class AssetsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assets
        fields = (
            'id',
            'hostname',
            'ip',
            'other_ip',
            'asset_type',
            'status',
            'os',
            'cpu_num',
            'memory',
            'disk',
            'sn',
            'usage',
            'application',
            'principal',
            'jira',
            'memo',
            'group',
            'idc',
        )