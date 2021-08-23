from users import models as user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    # MY USER
    name = models.CharField(null=False, blank=False, max_length=250)
    password = models.CharField(null=True, blank=False, max_length=250)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(null=True, max_length=250)

    def __str__(self):
        return self.name + " | " + str(self.phone)


class UserContact(models.Model):
    # Contacts that are imported from MY CONTACT LIST
    name = models.CharField(null=True, blank=False, max_length=250)
    phone = PhoneNumberField(null=True, blank=False)
    email = models.EmailField(null=True, max_length=250)
    spam_liklihood = models.IntegerField(null=True, default=0)
    imported_from = models.ForeignKey(
        to=User, on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        return self.name + " | " + str(self.phone) + " | " + str(self.spam_liklihood) + " %"
