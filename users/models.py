from django.db import models


# Create your models here.

# 用户表
class UserInfo(models.Model):
    email = models.EmailField(verbose_name='邮箱', max_length=25, primary_key=True)
    user = models.CharField(verbose_name='用户名', max_length=25)
    password = models.CharField(verbose_name='密码', max_length=125)
    CHOICES = ((0, '普通用户'), (1, 'VIP用户'), (2, '员工'))
    authority = models.IntegerField(verbose_name='权限', default=0, choices=CHOICES)

    def __str__(self):
        return self.user


# 员工信息表
class Employees(models.Model):
    number = models.CharField(verbose_name='员工编号', max_length=25)
    email = models.OneToOneField(verbose_name='邮箱', to=UserInfo, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='员工姓名', max_length=5)
    position = models.CharField(verbose_name='职位', max_length=6)
    merchant = models.ForeignKey(verbose_name='所属商家', to='home.Merchants', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ['number', 'merchant']


class UserToken(models.Model):
    user = models.OneToOneField(verbose_name='关联用户', to=UserInfo, to_field='email', on_delete=models.CASCADE)
    token = models.CharField(verbose_name='验证信息', max_length=128)
    # expire_time=models.DateTimeField()
