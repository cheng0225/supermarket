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



# from users import models
# from users.utils.一些类 import UserModelForm


# Create your views here.

class Up(GenericAPIView):
    serializer_class = URSerializer
    queryset = UserInfo.objects.all()

    def patch(self,request):
        # print(request.user.email,request.data)
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
        # request.data._mutable = True
        user=request.user
        # user.update(authority=2)
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

# from django.contrib.auth import models


# def login(request):
#     """ 登录 """
#     form = UserModelForm()
#     if request.method == 'POST':
#         form = UserModelForm(data=request.POST)
#         print(form)
#         if form.is_valid():
#             data_dict = form.cleaned_data
#             user_object = models.UserInfo.objects.filter(**data_dict).first()
#             if user_object:
#                 return redirect('users:index')
#     context = {'form': form}
#     return render(request, 'users/login.html', context)
#
#
# def logout(request):
#     """ 登出 """
#     return HttpResponse('登出')
#
#
# def register(request):
#     """ 注册 """
#     if request.method == 'GET':
#         form = UserModelForm()
#     else:
#         form = UserModelForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('users:index')
#     context = {'form': form}
#     return render(request, 'users/register.html', context)
#
#
# def index(request):
#     """ 主页 """
#     queryset = models.UserInfo.objects.all()
#     context = {'queryset': queryset}
#     return render(request, 'users/index.html', context)

    # if request.method == "GET":
    #     form = UserModelFrom()
    # else:
    #     form = UserModelFrom(data=request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('app02:user_list')
    # context = {'context': form}
    # return render(request, 'app02/user_add.html', context)
