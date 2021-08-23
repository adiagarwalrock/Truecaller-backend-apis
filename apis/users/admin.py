from .models import UserContact
from django.contrib import admin
from .models import User


# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'password']


# admin.site.register(UserContact)

@admin.register(UserContact)
class UserContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'spam_liklihood']
