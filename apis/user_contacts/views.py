# from django.http.response import JsonResponse

# from rest_framework.filters import SearchFilter                 # Search
# from rest_framework.parsers import JSONParser
# from rest_framework.decorators import api_view
# from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
# from rest_framework import status
# from .serializers import UserContactSerializer

# from .models import UserContact

# '''UserContact --> Views'''


# class ListUserContactAPIView(ListAPIView):
#     queryset = UserContact.objects.all()
#     serializer_class = UserContactSerializer

#     # search
#     # filter_backends = [SearchFilter]
#     # search_fields = ['phone', 'name']


# @api_view(['GET'])
# def fetch_single_user_contact_API_view(request, pk):
#     if request.method == 'GET':
#         try:
#             user_contacts = UserContact.objects.get(pk=pk)
#             user_contacts_serializer = UserContactSerializer(user_contacts)
#             return JsonResponse(user_contacts_serializer.data)
#         except UserContact.DoesNotExist:
#             return JsonResponse({'message': 'GET Request--> The User does not exist'}, status=status.HTTP_404_NOT_FOUND)


# class CreateUserContactAPIView(CreateAPIView):
#     queryset = UserContact.objects.all()
#     serializer_class = UserContactSerializer


# class UpdateUserContactAPIView(UpdateAPIView):
#     queryset = UserContact.objects.all()
#     serializer_class = UserContactSerializer


# @api_view(['DELETE'])
# def delete_user_contact_API_View(request, pk):
#     if request.method == 'DELETE':
#         try:
#             user_contacts = UserContact.objects.get(pk=pk)
#             user_contacts.delete()
#             return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
#         except UserContact.DoesNotExist:
#             return JsonResponse({'message': 'DELETE--> The User does not exist'}, status=status.HTTP_404_NOT_FOUND)


# @api_view(['GET', 'PUT'])
# def mark_spam_API_view(request, pk):
#     try:
#         user_contacts = UserContact.objects.get(pk=pk)
#         print(user_contacts)
#     except UserContact.DoesNotExist:
#         return JsonResponse({'message': 'The User does not exist'}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         user_contacts_data = JSONParser().parse(request)

#         user_contacts_serializer = UserContactSerializer(
#             user_contacts, data=user_contacts_data)
#         print(user_contacts_serializer, user_contacts_data)
#         print(user_contacts_serializer.is_valid())
#         if user_contacts_serializer.is_valid():
#             user_contacts_serializer.save()
#             return JsonResponse(user_contacts_serializer.data)
#         return JsonResponse(user_contacts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
