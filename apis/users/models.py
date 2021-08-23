from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    # MY USER
    name = models.CharField(null=False, blank=False, max_length=250)
    password = models.CharField(null=True, blank=False, max_length=250)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    email =  models.EmailField(null=True, max_length = 250)

    def __str__(self):
        return self.name + " | " + str(self.phone)


