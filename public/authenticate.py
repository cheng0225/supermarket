from rest_framework.authentication import BaseAuthentication
from django.contrib.auth import get_user_model
from users.models import UserToken

class MyAuth(BaseAuthentication):

    def authenticate(self, request):
        token=request.META.get('HTTP_TOKEN')
        user_token=UserToken.objects.filter(token=token).first()
        if user_token:
            return (user_token.user,token)
        return None

        # token=request.data.token
        # print('token')
        # print(request)
        # print(request.META.get('HTTP_TOKEN'))     # 获取请求头携带的token
        # print(user_token)
        # print((user_token.user))


# permission.py
from rest_framework.permissions import BasePermission
# 导入BasePermission
class MyPermission(BasePermission):
# 写权限类，继承BasePermission，内部重写has_permission
    def has_permission(self, request, view):
        user = request.user
        # 已经登陆，可以直接从request里面获取用户对象
        # print(user.get_user_type_display())
        # 可以拿到choices里面的中文字段
        print(user,user.authority)
        if user.authority == 2:
        # 自己写权限的逻辑（只有用户类型1的管理员可以访问这个视图）
            return True
        return False