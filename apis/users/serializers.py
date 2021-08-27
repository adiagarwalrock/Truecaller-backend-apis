from .models import UserContact
from .models import User

# from phonenumber_field.modelfields import PhoneNumberField

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class UserContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserContact
        fields = "__all__"


class ContactSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserContact
        fields = ['name', 'phone', 'spam_liklihood']


class UserSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['name', 'phone']
