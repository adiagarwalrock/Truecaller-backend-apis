import io
from django.http.response import JsonResponse

from .serializers import UserContactSerializer
from .serializers import UserSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
# from rest_framework.filters import SearchFilter                 # Search
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView

from .models import User, UserContact

'''User --> Views'''


class ListUserAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # Search
    # filter_backends = [SearchFilter]
    # search_fields = ['phone', 'name']


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


class ListUserContactAPIView(ListAPIView):
    queryset = UserContact.objects.all()
    serializer_class = UserContactSerializer
    # search
    # filter_backends = [SearchFilter]
    # search_fields = ['phone', 'name']


@api_view(['GET'])
def fetch_single_user_contact_API_view(request, pk):
    if request.method == 'GET':
        try:
            user_contacts = UserContact.objects.get(pk=pk)
            user_contacts_serializer = UserContactSerializer(user_contacts)
            return JsonResponse(user_contacts_serializer.data)
        except UserContact.DoesNotExist:
            return JsonResponse({'message': 'GET Request--> The User does not exist'}, status=status.HTTP_404_NOT_FOUND)


class CreateUserContactAPIView(CreateAPIView):
    queryset = UserContact.objects.all()
    serializer_class = UserContactSerializer


class UpdateUserContactAPIView(UpdateAPIView):
    queryset = UserContact.objects.all()
    serializer_class = UserContactSerializer


@api_view(['DELETE'])
def delete_user_contact_API_View(request, pk):
    if request.method == 'DELETE':
        try:
            user_contacts = UserContact.objects.get(pk=pk)
            user_contacts.delete()
            return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        except UserContact.DoesNotExist:
            return JsonResponse({'message': 'DELETE--> The User does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT'])
def mark_spam_API_view(request, pk):
    try:
        user_contacts = UserContact.objects.get(pk=pk)
        print(user_contacts)
    except UserContact.DoesNotExist:
        return JsonResponse({'message': 'The User does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        user_contacts_data = JSONParser().parse(request)

        user_contacts_serializer = UserContactSerializer(
            user_contacts, data=user_contacts_data)
        print(user_contacts_serializer, user_contacts_data)
        print(user_contacts_serializer.is_valid())
        if user_contacts_serializer.is_valid():
            user_contacts_serializer.save()
            return JsonResponse(user_contacts_serializer.data)
        return JsonResponse(user_contacts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def user_api(request):
    # Warning: Not Working
    # 111
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data)

    user = User.objects.all()
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data)
