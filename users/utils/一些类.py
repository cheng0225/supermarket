
from django.core.exceptions import ValidationError
from users.utils.encrypt import md5
from users import models
from django import forms

from django import forms
from users import models

class UserModelForm(forms.ModelForm):
    class Meta:
        model=models.UserInfo
        fields=['user','email','password']
        widgets={
            'user':forms.TextInput(),
            'email':forms.EmailInput(),
            'password':forms.PasswordInput(render_value=True)
        }
    def clean_password(self):
        pwd=self.cleaned_data.get('password')
        return md5(pwd)

#
# class LoginMF(forms.ModelForm):
#     class Meta:
#         model=models.UserInfo
#         # fields='__all__'
#         fields=['account','password']
#         widgets = {
#             'account':forms.TextInput(attrs={'class':'form-control'}),
#             'password':forms.PasswordInput(attrs={'class':'form-control'}),
#         }
#     def clean_password(self):
#         pwd=self.cleaned_data.get("password")
#         return md5(pwd)
#
#
# class UpMF(forms.ModelForm):
#     confirm_password=forms.CharField(label='确认密码',widget=forms.PasswordInput(render_value=True))
#     class Meta:
#         model=models.UserInfo
#         fields=['account','password','confirm_password']
#         widgets={
#             "password": forms.PasswordInput(render_value=True),
#         }
#
#     def clean_password(self):
#         pwd=self.cleaned_data.get("password")
#         return md5(pwd)
#
#     def clean_confirm_password(self):
#         pwd=self.cleaned_data.get("password")
#         confirm=md5(self.cleaned_data.get("confirm_password"))
#         # print(pwd,confirm)
#         if confirm!=pwd:
#             raise ValidationError("密码不一致")
#         return confirm