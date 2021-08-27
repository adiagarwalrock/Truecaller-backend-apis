from django.urls import path
# from django.views.decorators.csrf import csrf_exempt

from .views import delete_contact_api_view, update_contact_view, list_contact_view
from .views import CreateUserContactAPIView, mark_spam_view
from .views import CreateUserAPIView

from .views import list_user_view, update_user_view, delete_user_view

""" URLS --> contacts """


urlpatterns = [

    # '''User'''

    path("user/", list_user_view),
    path("user/<int:pk>/", list_user_view),

    path("create_user/", CreateUserAPIView.as_view(), name="user_create"),

    path("update_user/<int:pk>/", update_user_view),
    path("update_user/<int:pk>", update_user_view),

    path("delete_user/<int:pk>/", delete_user_view),
    path("delete_user/<int:pk>", delete_user_view),

    # '''Contacts'''

    path("contact/", list_contact_view),
    path("contact/<int:pk>/", list_contact_view),

    path("create_contact/", CreateUserContactAPIView.as_view(),
         name="user_contact_create"),

    path("update_contactxx/<int:pk>/", update_contact_view),
    path("update_contactxx/<int:pk>", update_contact_view),

    path("delete_contact/<int:pk>/", delete_contact_api_view),
    path("delete_contact/<int:pk>", delete_contact_api_view),

    path("mark_spam/<int:pk>/", mark_spam_view),
    path("mark_spam/<int:pk>", mark_spam_view),

    # '''Search'''


]


#     path("update_contact/<int:pk>/", UpdateUserContactAPIView.as_view(), name="user_contact_update"),
#     path("update_user/<int:pk>/", UpdateUserAPIView.as_view(), name="user_update"),
#     path("delete_user/<int:pk>/", DeleteUserAPIView.as_view(), name="user_delete"),
