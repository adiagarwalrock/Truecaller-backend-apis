from django.urls import path
from .views import ListUserAPIView
from .views import ListUserContactAPIView
from .views import global_search_view

""" URLS --> serach_engine """


urlpatterns = [
    path('contact/', ListUserContactAPIView.as_view()),

    path('user/', ListUserAPIView.as_view()),

    path('global/',global_search_view)
]
