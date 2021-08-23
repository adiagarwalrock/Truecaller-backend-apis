from django.urls import path

from .views import ListUserAPIView, CreateUserAPIView, UpdateUserAPIView, DeleteUserAPIView

"""
application URLS--> contacts 
"""

urlpatterns = [
    path("list_user/",ListUserAPIView.as_view(),name="user_list"),

    path("create_user/", CreateUserAPIView.as_view(),name="user_create"),

    path("update_user/<int:pk>/",UpdateUserAPIView.as_view(),name="user_update"),

    path("delete_user/<int:pk>/",DeleteUserAPIView.as_view(),name="user_delete"),
]