#! /usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from models import NAVI


class NAVISerializer(serializers.HyperlinkedModelSerializer):
    """
    继承serializers.ModelSerializer，fields为API想要得到的字段。
    """
    class Meta:
        model = NAVI
        # fields = '__all__'
        fields = ('id', 'name', 'description','url','memo')
