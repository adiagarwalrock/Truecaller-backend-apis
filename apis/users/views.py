from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import UserSerializer

from .models import User

class ListUserAPIView(ListAPIView):
    """This endpoint list all of the available Users from the database"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateUserAPIView(CreateAPIView):
    """This endpoint allows for creation of a User"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UpdateUserAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific User by passing in the id of the User to update"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DeleteUserAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific User from the database"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
