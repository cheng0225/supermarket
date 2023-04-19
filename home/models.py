from django.db import models
import os

# import users.models

# Create your models here.

# 商家表
class Merchants(models.Model):
    number = models.CharField(verbose_name='商家编号', primary_key=True, max_length=25)
    name = models.CharField(verbose_name='商家名称', max_length=12)
    address = models.CharField(verbose_name='商家地址', max_length=25)
    latlon = models.CharField(verbose_name='经纬度',max_length=52)

    def __str__(self):
        return self.name


# 商品表
MEDIA_ADDR = 'http://localhost:8000/media/'

def img_path(instance,filename):
    # print(instance,filename)
    # return os.path.join('ThingImg',instance.merchant,filename)
    img_name=f'{instance.number}.{filename.split(".")[-1]}'   # 文件 图片名字 完整后缀
    sj=instance.merchant.number   # 获取商家编号  因为店名不一定唯一
    return os.path.join('ThingImg',sj,img_name) # 拼接返回

class Things(models.Model):
    number = models.CharField(verbose_name='商品编号', max_length=25)
    merchant = models.ForeignKey(verbose_name='所属商家', to=Merchants, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='商品名称', max_length=12)
    num = models.SmallIntegerField(verbose_name='商品库存数量')  # -32768 到 32767
    price = models.DecimalField(verbose_name='商品单价', max_digits=8, decimal_places=2)
    kind = models.CharField(verbose_name='商品类型', max_length=12)
    position = models.CharField(verbose_name='商品位置', max_length=12)
    img = models.ImageField(verbose_name='商品图片',upload_to=img_path)

    class Meta:
        unique_together = ['number', 'merchant']

    def __str__(self):
        return self.name

    def get_img_url(self):
        """返回图片的url"""
        return MEDIA_ADDR + str(self.img)


# 用户订单表
class Orders(models.Model):
    email = models.ForeignKey(verbose_name='用户邮箱', to='users.UserInfo', on_delete=models.CASCADE)
    merchant = models.ForeignKey(verbose_name='所属商家', to=Merchants, on_delete=models.CASCADE)
    thing = models.ForeignKey(verbose_name='商品', to=Things, on_delete=models.CASCADE)
    time = models.DateTimeField(verbose_name='购买时间', auto_now_add=True)
    num = models.SmallIntegerField(verbose_name='购买数量')  # -32768 到 32767
    cost = models.DecimalField(verbose_name='支付金额', max_digits=8, decimal_places=2)

    class Meta:
        unique_together = ['email', 'merchant', 'thing', 'time']


# 员工操作记录表
class Logs(models.Model):
    employee = models.ForeignKey(verbose_name='员工编号', to='users.Employees', on_delete=models.CASCADE)
    merchant = models.ForeignKey(verbose_name='所属商家', to=Merchants, on_delete=models.CASCADE)
    time = models.DateTimeField(verbose_name='修改时间', auto_now_add=True)
    txt = models.CharField(verbose_name='操作说明', max_length=125)

    class Meta:
        unique_together = ['employee', 'merchant', 'time']
