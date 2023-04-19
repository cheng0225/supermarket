from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed
from users.models import UserToken


class MyAuth(BaseAuthentication):
    """ 验证token 看是否已经登录 """
    def authenticate(self, request):
        # print("正在认证检测 是否登录",)  #token
        token = request.META.get('HTTP_TOKEN')
        user_token = UserToken.objects.filter(token=token).first()
        if user_token:
            return user_token.user, token
        # return None
        raise AuthenticationFailed('请先登录')


# class UPermit(BasePermission):
#     """  检测权限是否属于登录用户 """
#     def has_permission(self, request, view):
#         user = request.user
#         # print(user)      pychan抱怨报错类型宽泛
#         # noinspection PyBroadException
#         try:
#             k = user.authority
#             return True
#         except Exception as e:
#             return False

# class MPermit(BasePermission):
#     """  检测权限是否属于商家 """
#     def has_permission(self, request, view):
#         user = request.user
#         # print(user)      pychan抱怨报错类型宽泛
#         # noinspection PyBroadException
#         if user.authority
#             return True
#         except Exception as e:
#             return False

class EPermit(BasePermission):
    """  检测权限是否属于员工 """
    def has_permission(self, request, view):
        user = request.user
        # print(user)      pychan抱怨报错类型宽泛
        # noinspection PyBroadException
        if user.authority == 2:
            return True
        return False