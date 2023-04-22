from django.urls import path
from users.views import Register, Login, Up, Emp

app_name = 'users'
urlpatterns = [
    path(r'register',Register.as_view()),
    path(r'login',Login.as_view()),
    path(r'up',Up.as_view()),
    path(r'emp',Emp.as_view()),
]
