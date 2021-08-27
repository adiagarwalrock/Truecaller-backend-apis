from django.db.models import F
import io
from django.http.response import JsonResponse
from django.views.decorators.http import require_POST

from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .serializers import UserContactSerializer, UserSerializer
from .models import User, UserContact


'''####################'''
'''USER'''
'''####################'''


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
    # Updates any user field by referencing the user-id
    if request.method == 'PUT':
        user = User.objects.get(pk=pk)
        user_data = JSONParser().parse(request)

        user_serializer = UserSerializer(user, partial=True, data=user_data)

        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse({'message': 'User was updated successfully!'}, status=status.HTTP_200_OK)
        return JsonResponse({'message': 'User could not be updated successfully!', 'request_type': 'PUT', 'function': 'update_user_view'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CreateUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['DELETE'])
def delete_user_view(request, pk):
    if request.method == 'DELETE':
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return JsonResponse({'message': 'User deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return JsonResponse({'message': 'User does not exist', 'request_type': 'DELETE', 'function': 'delete_user_view'}, status=status.HTTP_404_NOT_FOUND)


'''####################'''
''' CONTACTS'''
'''####################'''


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


class CreateUserContactAPIView(generics.CreateAPIView):
    queryset = UserContact.objects.all()
    serializer_class = UserContactSerializer


@api_view(['PUT'])
def update_contact_view(request, pk):
    # Updates any contact field by referencing the user-id
    if request.method == 'PUT':
        contact = UserContact.objects.get(pk=pk)
        contact_data = JSONParser().parse(request)

        contact_serializer = UserContactSerializer(
            contact, partial=True, data=contact_data)

        if contact_serializer.is_valid():
            contact_serializer.save()
            return JsonResponse({'message': 'contact was updated successfully!'}, status=status.HTTP_200_OK)
        return JsonResponse({'message': 'contact could not be updated successfully!', 'request_type': 'PUT', 'function': 'update_user_view'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def delete_contact_api_view(request, pk):
    if request.method == 'DELETE':
        try:
            contact = UserContact.objects.get(pk=pk)
            contact.delete()
            return JsonResponse({'message': 'Contact was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        except UserContact.DoesNotExist:
            return JsonResponse({'message': 'Contact does not exist', 'request_type': 'DELETE', 'function': 'delete_contact_view'}, status=status.HTTP_404_NOT_FOUND)


'''####################'''
'''MARK SPAM'''
'''####################'''


@api_view(['PATCH', 'GET'])
def mark_spam_view(request, pk):
    UserContact.objects.filter(pk=pk).update(
        spam_liklihood=F('spam_liklihood')+1)
    try:
        contact = UserContact.objects.get(pk=pk)
        contact_serializer = UserContactSerializer(contact)
        return JsonResponse(contact_serializer.data, status=status.HTTP_302_FOUND)
    except UserContact.DoesNotExist:
        return JsonResponse({'message': 'The contact does not exist', 'request_type': 'GET', 'function': 'mark_spam_view'}, status=status.HTTP_404_NOT_FOUND)
