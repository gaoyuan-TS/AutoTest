from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from user_app.serializers import *
from user_app.models import UserInfo
from utils.Token import Token

import logs
import hashlib
# Create your views here.


"""
根据用户名密码登录
"""
class UserLogin(APIView):
    def post(self,request):
        user = request.data
        username = user["username"]
        password = user["password"]
        token = Token(username).get_token()
        try:
            userinfo = UserInfo.objects.get(name =username ,password=password)
            return Response({'code': 200, 'msg': 'success','token':token})
        except:
            return Response({'code': 401, 'msg': 'false','data': "用户名/密码不正确"})


"""
获取所有用户列表
"""


class UserList(APIView):
    def get(self, request):
        # queryset = UserInfo.objects.all()
        # ret = UserSerializerAll(queryset,many=True)

        queryset = UserInfo.objects.filter(is_delete=0)
        response = {'code': 200, 'msg': 'success', 'total': '', 'data': []}
        ret = UserSerializerOther(queryset, many=True)
        response['data'] = ret.data
        response['total'] = len(ret.data)
        return Response(response)


"""
、根据用户ID查询用户信息
"""


class UserSingById(APIView):
    def get(self, request, pk):
        try:
            userinfo = UserInfo.objects.get(id=pk)
        except:
            return Response({"message": "该用户不存在"})
        user = UserSerializerOther(userinfo)
        # data = {
        #     'id' : userinfo.id,
        #     'name': userinfo.name,
        #     'email':userinfo.email,
        #     'mobile':userinfo.mobile,
        #     'sex':userinfo.sex,
        #     'creat_time':userinfo.creat_time
        #
        # }
        return Response({'code': 200, 'msg': 'success','data': user.data})


"""
添加用户
"""


class AddUser(APIView):
    def post(self, request):
        data = request.data
        user = UserSerializerAll(data=request.data)
        # response = {'code': 200, 'msg': 'success', 'data': user.data}
        if user.is_valid():
            user.save()
            return Response(user.data)
        else:
            return Response(user.errors)


"""
根据用户ID删除
"""


class DelectUserById(APIView):
    def post(self, request, pk):
        try:
            user = UserInfo.objects.get(id=pk)
        except:
            return Response({"message": "该用户已删除"})
        else:
            user.is_delete = 1
            user.save()
            return Response({"code": 200, "message": "删除成功"})


"""
根据用户ID更新信息
"""


class UpdataUserById(APIView):
    def post(self, request, pk):
        try:
            user = UserInfo.objects.get(id=pk)
        except:
            return Response({"message": "该用户不存在"})

        ser = UserSerializerOther(user, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"code": 200, "message": "修改成功", "data": ser.data})
        return Response({"message": ser.errors})


"""
根据ID查询单个用户详请
"""


class UserDetail(generics.RetrieveAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializerAll

# class UserIndex(APIView):
#     def get(self,request):
#         queryset1 = UserInfo.objects.values('name','mobile','email','sex')
#         ret = UserSerializerOther(queryset1, many=True)
#         return render(request,'index.html',ret)

# json.dumps(result), content_type="application/json"
