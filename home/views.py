# from django.shortcuts import render

# Create your views here.
from rest_framework.mixins import *
from rest_framework.views import APIView
from home.serializer import *
from home.models import *
from rest_framework.generics import *
from rest_framework.response import Response
from users.models import Employees


class ThingsView(GenericAPIView, ListModelMixin, CreateModelMixin):
    """ 商品视图 """
    authentication_classes = []  # 不做认证
    permission_classes = []  # 不做任何权限限制
    queryset = Things.objects.all()
    serializer_class = ThingsSerializer

    def get(self, request):
        return self.list(request)



from public import AuthPermit


class AddThings(GenericAPIView, ListModelMixin, CreateModelMixin):
    """ 添加商品 做员工认证 并自动绑定该商品到当前员工所属商家 """
    permission_classes = [AuthPermit.EPermit]
    queryset = Things.objects.all()
    serializer_class = ThingsSerializer

    def post(self, request):
        # print('data', request.data)
        request.data._mutable = True
        email =request.user.email
        # print('user', request.user.Employees_set().all())
        # print('user', request.user.merchant)
        emp = Employees.objects.filter(email=email).first()
        # print(emp)
        request.data['merchant'] = emp.merchant.number
        # print(request.data)
        return self.create(request)

    def put(self,request):
        """ 更新商品信息需要管理员身份 """
        print('put',request.data)
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        return Response(ser.data)

    def patch(self,request):
        """ 更新部分数据  同时自动生成员工操作日志 """
        data = request.data
        data._mutable = True
        # print('patch data',request.data) # type(request.data.img))
        print(type(request.data.__getitem__('img')))
        if type(data.get('img',0)) is str:
            data.pop('img')
        id = data.get('id')
        things = Things.objects.filter(id=id).first()
        ser = self.get_serializer(instance=things,data=data)
        ser.is_valid(raise_exception=True)
        ser.save()
        # print(ser.validated_data, request.data)
        # print('ser',ser,type(ser.img))
        user = request.user
        # print(type(user))
        em = user.employees
        # print(em)
        form = {
            "employee": em,
            "merchant": em.merchant,
            "txt": data.get('txt')
        }
        # print(form)
        Logs.objects.create(**form)
        return Response(ser.data)



class MerchantsView(GenericAPIView, CreateModelMixin, UpdateModelMixin):
    """ 针对商家的视图 """
    queryset = Merchants.objects.all()
    serializer_class = MerchantsSerializer
    authentication_classes = []  # 不做认证
    permission_classes = []  # 不做任何权限限制

    def get(self, request):
        """ 获取所有商家信息 """
        serializer = self.get_serializer(instance=self.get_queryset(), many=True)
        return Response(serializer.data)
        # return Response()

    def post(self, request):
        print(request.data)
        """ 新增商家 """
        return self.create(request)

    def put(self, request):
        """ 更新商家信息 """
        obj = Merchants.objects.filter(number=request.data['number'])[0]
        # print(request.data,obj)  查说是filter获取对象 取第一个
        serializer = MerchantsSerializer(instance=obj, data=request.data)
        # print(serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# Orders
class OrdersView(ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

    # def get(self,request):
    #     return self.list(request)
    #
    # def post(self,request):
    #     return self.create(request)


# Log
class LogsView(ListCreateAPIView):
    """ 员工操作日志 """
    queryset = Logs.objects.all()
    serializer_class = LogsSerializer
    permission_classes = [AuthPermit.EPermit]

    # def get(self,request):
    #     """ 返回所有记录 """
    #     return self.list(request)
    #
    # def post(self,request):
    #     """ 新的操作记录 """
    #     return self.create(request)


class SearchView(GenericAPIView):
    """ 针对商品查询视图 """
    # 对于多余参数 现在还没有处理 序列化直接忽略
    # queryset =
    serializer_class = MerchantsSerializer

    def get(self, request):
        # print(request.data)
        # request.GET==request.query_params
        # obj=Things.objects.filter(**request.query_params)
        params = request.query_params  # .dict()
        print(params)
        serializer = self.get_serializer(data=params)
        serializer.is_valid(raise_exception=False)
        # obj=Merchants.objects.filter(**serializer.data)
        # serializer=self.get_serializer(instance=obj,many=True)
        return Response(serializer.data)


class LatLon(GenericAPIView):
    """ 获取经纬度  （某个商家） """
    authentication_classes = []  # 不做认证
    permission_classes = []  # 不做任何权限限制
    serializer_class = LatLonSerializer

    def get(self, request):
        # print(request.query_params)
        f = self.serializer_class(data=request.query_params)
        # print(request.query_params, f.data)
        f.is_valid(raise_exception=True)
        # print(f.data)
        thing = Things.objects.filter(**f.data).first()
        # print(thing,thing.merchant.number)
        merchant = Merchants.objects.filter(number=thing.merchant.number).first()
        # print(merchant)
        form = MerchantsSerializer(instance=merchant)
        # print(form.data)
        return Response(form.data)



# class ThingsView(APIView):
#     """ 商品视图 """
#     authentication_classes = []  # 不做认证
#     permission_classes = [] # 不做任何权限限制
#     def get(self, request):
#         things = Things.objects.all()
#         serializer = ThingsSerializer(instance=things, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         data = request.data
#         serializer = ThingsSerializer(data=data)
#         # 哦 原来这个设置true 会自动返回错误  要学会多看看源码
#         serializer.is_valid(raise_exception=True)
#         # img = request.FILES['avatar_file']  # 获取上传图片
#         # cropped_avatar = crop_image(img, user.id)
#         # user_profile.avatar = cropped_avatar  # 将图片路径修改到当前会员数据库
#         serializer.save()
#         return Response(serializer.data)
#
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     return Response(serializer.data)
#         # return Response(serializer.errors)