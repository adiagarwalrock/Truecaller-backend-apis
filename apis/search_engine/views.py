from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

from users.models import User, UserContact
from users.serializers import UserSerializer, UserContactSerializer

'''Search_Engine --> Views'''


class ListUserContactAPIView(ListAPIView):
    queryset = UserContact.objects.all()
    serializer_class = UserContactSerializer
    filter_backends = [SearchFilter]
    search_fields = ['phone', 'name']


class GlobalSearch(ListAPIView):
    pass


class DynamicSearchFilter(SearchFilter):

    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class ListUserAPIView(ListAPIView):
    filter_backends = [DynamicSearchFilter]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = ['phone', 'name']


def global_search_view():
    return