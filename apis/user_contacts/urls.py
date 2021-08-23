from django.urls import path

from .views import ListUserContactAPIView, CreateUserContactAPIView, UpdateUserContactAPIView, mark_spam_API_view
from .views import fetch_single_user_contact_API_view, delete_user_contact_API_View


""" application URLS--> users """

urlpatterns = [
    path("list_contact/",ListUserContactAPIView.as_view(),name="user_contact_list"),

    path("fetch_contact/<int:pk>/", fetch_single_user_contact_API_view),

    path("create_contact/", CreateUserContactAPIView.as_view(),name="user_contact_create"),

    path("update_contact/<int:pk>/",UpdateUserContactAPIView.as_view(),name="user_contact_update"),

    path("delete_contact/<int:pk>/",delete_user_contact_API_View),

    path("mark_spam/<int:pk>/",mark_spam_API_view),
]