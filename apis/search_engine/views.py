from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

from users.models import User, UserContact
from users.serializers import UserSerializer, UserContactSerializer
# from user_contacts.models import UserContact,
# from user_contacts.serializers import UserContactSerializer

'''Search_Engine --> Views'''


class ListUserContactAPIView(ListAPIView):
    queryset = UserContact.objects.all()
    serializer_class = UserContactSerializer
    filter_backends = [SearchFilter]
    search_fields = ['phone', 'name']


class ListUserAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter]
    search_fields = ['phone', 'name']
