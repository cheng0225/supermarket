import os
import uuid

from django.shortcuts import render, redirect, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework import status
from users.serializer import UserSerializer, URSerializer, EmpSerializer
from users.models import UserInfo,UserToken, Employees



# Create your views here.

class Up(GenericAPIView):
    serializer_class = URSerializer
    queryset = UserInfo.objects.all()

    def patch(self,request):
        request.data['email'] = request.user.email
        ser = self.serializer_class(instance=request.user,data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)


class Emp(GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = EmpSerializer
    queryset = Employees.objects.all()

    def post(self, request):
        """ 员工认证 拿到信息 自动绑定当前账号邮箱 并改权限为2 """
        user=request.user
        user.authority=2
        user.save()
        email = user.email
        request.data['email'] = email
        return self.create(request)


class Register(APIView):
    authentication_classes = []  # 不做认证
    permission_classes = [] # 不做任何权限限制

    def get(self,request):
        q=UserInfo.objects.all()
        serializer=UserSerializer(instance=q,many=True)
        return Response(serializer.data)

    def post(self,request):
        data=request.data
        serializer=URSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class Login(GenericAPIView):
    authentication_classes = []  # 不做认证
    permission_classes = [] # 不做任何权限限制

    def get(self,request):
        """ get 可以不需要 前端自己完成"""
        q=UserInfo.objects.all()
        serializer=UserSerializer(instance=q,many=True)
        return Response(serializer.data)

    def post(self,request):
        """ 获取信息 校验 生成token 基于存储形式 更新或者创建token"""
        print('post 登录',request.data)
        res={'code':1, 'msg':'用户名或密码错误', 'user': None, 'token': None}
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_obj=UserInfo.objects.filter(**serializer.data).first()
        print(user_obj)
        if user_obj:
            res['code']=0
            res['msg']=0
            res['user']=user_obj.user
            random_str=uuid.uuid4()
            # random_str=os.urandom(16) 两种方法
            UserToken.objects.update_or_create(user=user_obj,defaults={'token':random_str})
            res['token']=random_str
            return Response(res)
        return Response(res,status=status.HTTP_401_UNAUTHORIZED)
