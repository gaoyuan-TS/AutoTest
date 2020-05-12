from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from test_case.models import TestCase
from test_case.serializers import TestCaseSerializerAll
from user_app.serializers import *
from user_app.models import UserInfo
# Create your views here.

"""
获取所有测试用例
"""

class TestCaseList(APIView):
    def get(self,request):
        # queryset = UserInfo.objects.all()
        # ret = UserSerializerAll(queryset,many=True)

        queryset=TestCase.objects.all()
        response = {'code': 200, 'msg': 'success', 'total': '', 'data':[]}
        ret = TestCaseSerializerAll(queryset, many=True)
        response['data']= ret.data
        response['total'] = len(ret.data)
        return Response(response)


class TestCaseAdd(APIView):
    def post(self,request):
        testcase = TestCaseSerializerAll(data=request.data)
        if testcase.is_valid():
            testcase.save()
            return Response(testcase.data)
        else:
            return Response(testcase.errors)





class TestDetailById(generics.RetrieveAPIView):
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializerAll