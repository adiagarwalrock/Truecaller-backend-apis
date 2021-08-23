from .models import UserContact
from .models import User

from phonenumber_field.modelfields import PhoneNumberField

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class UserContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserContact
        fields = "__all__"


class UserSerializer(serializers.Serializer):
    # Warning
    name = serializers.CharField(max_length=250)
    password = serializers.CharField(max_length=250)
    phone = PhoneNumberField(unique=True)
    email = serializers.EmailField(max_length=250)
    pass
