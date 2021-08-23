from rest_framework import serializers
from .models import UserContacts


class UserContactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserContacts
        fields = "__all__"