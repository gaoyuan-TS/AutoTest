#!/usr/bin/env python
# encoding: utf-8
"""
@author :gaoyuan
@contact:1103313679@qq.com
@time   :2020/4/30 10:17
"""
from rest_framework import serializers
from user_app.models import *
from test_case.models import *
from test_case.serializers import *


class UserSerializerAll(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UserInfo
        extra_kwargs = {'id': {'required': False}}


class UserSerializerOther(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'mobile', 'email', 'sex']
        model = UserInfo
        extra_kwargs = {'id': {'required': False}}

