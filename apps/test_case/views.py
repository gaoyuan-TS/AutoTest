from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from test_case.models import TestCase
from test_case.serializers import TestCaseSerializerAll
from user_app.serializers import *
from user_app.models import UserInfo
from test_case.testcase import *
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


"""
运行EXCEL测试用用例
"""

class TestRunner(APIView):
    def get(self,request):
        RunnerTestCase().RunnerBeautifulReport()
        return Response({"message":"运行testcasec结束"})

    def post(self,request):
        ts_detail = TestCaseDetailSerializer(data=request.data)
        if ts_detail.is_valid():
            ts_detail.save()
        data =request.data
        ip = data.get('ip')
        browser = data.get('browser')
        Version = data.get('Version')
        loop = data.get('loop')
        report_address = data.get('report_address')
        importAddress = data.get('importAddress')
        moudle = data.get('moudle')

        file = CONFIG_PATH+'Parameter.yaml'
        YamlWrite().Write_Yaml_Updata(file, 'IP', ip)
        YamlWrite().Write_Yaml_Updata(file, 'Browser', browser)
        YamlWrite().Write_Yaml_Updata(file, 'ReportAddress', report_address)
        YamlWrite().Write_Yaml_Updata(file, 'loop', loop)
        YamlWrite().Write_Yaml_Updata(file, 'ImportAddress', importAddress)
        YamlWrite().Write_Yaml_Updata(file, 'Moudle', moudle)
        YamlWrite().Write_Yaml_Updata(file, 'Version', Version)
        YamlWrite().Write_Yaml_Updata(file, 'CaseNum', 1)


        RunnerTestCase().RunnerBeautifulReport()
        return Response({'code': 200, 'msg': '测试用例运行结束', 'data':ts_detail.data})


class TestDetailById(generics.RetrieveAPIView):
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializerAll