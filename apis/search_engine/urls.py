from django.urls import path
from .views import ListUserAPIView
from .views import ListUserContactAPIView

""" URLS --> serach_engine """


urlpatterns = [
    path('contact/', ListUserContactAPIView.as_view()),

    path('user/', ListUserAPIView.as_view()),
]
