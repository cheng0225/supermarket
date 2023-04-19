from rest_framework.serializers import *
# from rest_framework import
from home.models import *


class ThingsSerializer(ModelSerializer):
    img = ImageField(label='商品图片', max_length=100, allow_null=True, default=None)
    # txt = CharField(label='备注', max_length=125, default=None, allow_blank=True)
    class Meta:
        model = Things
        fields = '__all__'


# class UpThingsSerializer(ModelSerializer):
#     id = IntegerField(label='ID', read_only=True)
#     img = ImageField(allow_null=True, default=None, label='商品图片', max_length=100)
#     number = CharField(label='商品编号', max_length=25, required=True)
#     num = IntegerField(label='商品库存数量', max_value=32767, min_value=-32768)
#     price = DecimalField(decimal_places=2, label='商品单价', max_digits=8)
#     kind = CharField(label='商品类型', max_length=12)
#     position = CharField(label='商品位置', max_length=12)
#     merchant = PrimaryKeyRelatedField(label='所属商家', queryset=Merchants.objects.all(), required=True)
#     class Meta:
#         model = Things
#         fields = '__all__'
    #     validators = [<UniqueTogetherValidator(queryset=Things.objects.all(), fields=('number', 'merchant'))>]


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
