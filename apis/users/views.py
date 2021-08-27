import io
from django.http.response import JsonResponse
from rest_framework.response import Response

from .serializers import UserContactSerializer
from .serializers import UserSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.filters import SearchFilter                 # Search
# from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView

from .models import User, UserContact

'''User --> Views'''


@api_view(['GET'])
def list_user_view(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            try:
                user = User.objects.get(pk=pk)
                user_serializer = UserSerializer(user)
                return JsonResponse(user_serializer.data, status=status.HTTP_302_FOUND)
            except User.DoesNotExist:
                return JsonResponse({'message': 'The User does not exist', 'request_type': 'GET', 'function': 'list_user_api_view'}, status=status.HTTP_404_NOT_FOUND)
        else:
            user_obj = User.objects.all()
            user_serializer = UserSerializer(user_obj, many=True)
            return JsonResponse(user_serializer.data, safe=False, status=status.HTTP_302_FOUND)


@api_view(['PUT'])
def update_user_view(request, pk):
    if request.method == 'PUT':
        user = User.objects.get(pk=pk)
        user_data = JSONParser().parse(request)

        user_serializer = UserSerializer(user, partial=True, data=user_data)

        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse({'message': 'User was updated successfully!'}, status=status.HTTP_200_OK)
        return JsonResponse({'message': 'User could not be updated successfully!', 'request_type': 'PUT', 'function': 'update_user_view'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CreateUserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UpdateUserAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeleteUserAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def list_contact_view(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            try:
                contact = UserContact.objects.get(pk=pk)
                contact_serializer = UserContactSerializer(contact)
                return JsonResponse(contact_serializer.data, status=status.HTTP_302_FOUND)
            except UserContact.DoesNotExist:
                return JsonResponse({'message': 'The User does not exist', 'request_type': 'GET', 'function': 'list_user_api_view'}, status=status.HTTP_404_NOT_FOUND)
        else:
            contact_obj = UserContact.objects.all()
            contact_serializer = UserContactSerializer(contact_obj, many=True)
            return JsonResponse(contact_serializer.data, safe=False, status=status.HTTP_302_FOUND)


class CreateUserContactAPIView(CreateAPIView):
    queryset = UserContact.objects.all()
    serializer_class = UserContactSerializer


class UpdateUserContactAPIView(UpdateAPIView):
    queryset = UserContact.objects.all()
    serializer_class = UserContactSerializer


@api_view(['DELETE'])
def delete_contact_api_view(request, pk):
    if request.method == 'DELETE':
        try:
            contact = UserContact.objects.get(pk=pk)
            contact.delete()
            return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        except UserContact.DoesNotExist:
            return JsonResponse({'message': 'DELETE--> The User does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT'])
def mark_spam_view(request, pk):
    # print(type(request))
    # print("REQUEST: ", type(request.data))
    # request["data"] = {"spam_liklihood": 99}

    try:
        contact = UserContact.objects.get(pk=pk)
        print("contact: ", contact)

    except UserContact.DoesNotExist:
        return JsonResponse({'message': 'The User does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        contact_data = JSONParser().parse(request)

        contact_serializer = UserContactSerializer(
            contact, data=contact_data)
        # print(contact_serializer, contact_data)
        print("T&F: ", contact_serializer.is_valid())

        if contact_serializer.is_valid():
            contact_serializer.save()
            return JsonResponse(contact_serializer.data)
        return JsonResponse(contact_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
