from rest_framework.serializers import *
# from rest_framework import
from home.models import *


class ThingsSerializer(ModelSerializer):
    img = ImageField(label='商品图片', max_length=100, allow_null=True, default=None)
    # txt = CharField(label='备注', max_length=125, default=None, allow_blank=True)
    class Meta:
        model = Things
        fields = '__all__'


class MerchantsSerializer(ModelSerializer):
    class Meta:
        model = Merchants
        fields = '__all__'


class LogsSerializer(ModelSerializer):
    class Meta:
        model = Logs
        fields = '__all__'


class OrdersSerializer(ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class LatLonSerializer(ModelSerializer):
    id = IntegerField(label='ID')
    class Meta:
        model = Things
        fields = ['id']
