from django.http.response import JsonResponse
from django import template
from django.db.models import Q
from django.views.generic import ListView

from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

from itertools import chain

from users.models import User, UserContact
from users.serializers import UserSerializer, UserContactSerializer
from users.serializers import UserSearchSerializer, ContactSearchSerializer

'''Search_Engine --> Views'''


class ListUserContactAPIView(ListAPIView):
    filter_backends = [SearchFilter]
    queryset = UserContact.objects.all()
    serializer_class = ContactSearchSerializer
    search_fields = ['phone', 'name']


class GlobalSearchView(ListView):

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
        if query is not None:
            user_results = User.objects.search(query=query)
            contact_results = UserContact.objects.search(query=query)
            queryset_chain = chain(
                user_results,
                contact_results
            )
            query_search = sorted(queryset_chain,
                                  key=lambda instance: instance.pk,
                                  reverse=True)
            self.count = len(query_search)
            return JsonResponse({"results": list(query_search)}, safe=False)
        return User.objects.none()


class ListUserAPIView(ListAPIView):
    filter_backends = [SearchFilter]
    queryset = User.objects.all()
    serializer_class = UserSearchSerializer
    search_fields = ['phone', 'name']


class SearchForUsers(ListAPIView):
    serializer_class = ContactSearchSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        queryset = UserContact.objects.all()
        queryset_starts_with = queryset.filter(name__istartswith=name)
        queryset_contains = queryset.filter(name__icontains=name)


def global_search_view():
    return
