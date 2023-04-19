from rest_framework.serializers import Serializer, ModelSerializer,ChoiceField
from rest_framework import serializers
from users.models import UserInfo, Employees


class UserSerializer(ModelSerializer):
    authority = ChoiceField(choices=UserInfo.CHOICES, source="get_authority_display", read_only=True)
    email = serializers.EmailField(label='邮箱', max_length=25)
    user = serializers.CharField(read_only=True)   # write_only
    class Meta:
        model = UserInfo
        fields = '__all__'

class URSerializer(ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'

class EmpSerializer(ModelSerializer):
    # email = serializers.EmailField(blank=True)
    class Meta:
        model = Employees
        fields = '__all__'