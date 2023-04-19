from django.urls import path
from users.views import Register, Login, Up, Emp

app_name = 'users'
urlpatterns = [
    path(r'register',Register.as_view()),
    path(r'login',Login.as_view()),
    path(r'up',Up.as_view()),
    path(r'emp',Emp.as_view()),

    # path('',views.index,name='index'),
    # path('login/',views.login,name='login'),  # 登录
    # path('logout/',views.logout,name='logout'),  # 登出
    # path('register/',views.register,name='register'),  # 注册
]
