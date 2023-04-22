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
        request.data._mutable = True
        email =request.user.email
        emp = Employees.objects.filter(email=email).first()
        request.data['merchant'] = emp.merchant.number
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
        print(type(request.data.__getitem__('img')))
        if type(data.get('img',0)) is str:
            data.pop('img')
        id = data.get('id')
        things = Things.objects.filter(id=id).first()
        ser = self.get_serializer(instance=things,data=data)
        ser.is_valid(raise_exception=True)
        ser.save()
        user = request.user
        em = user.employees
        form = {
            "employee": em,
            "merchant": em.merchant,
            "txt": data.get('txt')
        }
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

    def post(self, request):
        print(request.data)
        """ 新增商家 """
        return self.create(request)

    def put(self, request):
        """ 更新商家信息 """
        obj = Merchants.objects.filter(number=request.data['number'])[0]
        serializer = MerchantsSerializer(instance=obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# Orders
class OrdersView(ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

# Log
class LogsView(ListCreateAPIView):
    """ 员工操作日志 """
    queryset = Logs.objects.all()
    serializer_class = LogsSerializer
    permission_classes = [AuthPermit.EPermit]


class SearchView(GenericAPIView):
    """ 针对商品查询视图 """
    # 对于多余参数 现在还没有处理 序列化直接忽略
    # queryset =
    serializer_class = MerchantsSerializer

    def get(self, request):
        params = request.query_params  # .dict()
        print(params)
        serializer = self.get_serializer(data=params)
        serializer.is_valid(raise_exception=False)
        return Response(serializer.data)


class LatLon(GenericAPIView):
    """ 获取经纬度  （某个商家） """
    authentication_classes = []  # 不做认证
    permission_classes = []  # 不做任何权限限制
    serializer_class = LatLonSerializer

    def get(self, request):
        f = self.serializer_class(data=request.query_params)
        f.is_valid(raise_exception=True)
        thing = Things.objects.filter(**f.data).first()
        merchant = Merchants.objects.filter(number=thing.merchant.number).first()
        form = MerchantsSerializer(instance=merchant)
        return Response(form.data)

