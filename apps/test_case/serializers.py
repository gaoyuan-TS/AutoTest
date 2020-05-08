#!/usr/bin/env python
# encoding: utf-8
"""
@author :gaoyuan
@contact:1103313679@qq.com
@time   :2020/4/30 10:17
"""
from rest_framework import serializers
from test_case.models import *
from user_app.models import *

class TestCaseSerializerAll(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = TestCase
        extra_kwargs = {'id': {'required': False}}



class TestCaseSerializerOther(serializers.ModelSerializer):
    class Meta:
        fields = ['id','user_id','test_name','test_type','creat_time','']
        model = TestCase
        extra_kwargs = {'id': {'required': False}}
        # depth=1