# from users import models as user_model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.query_utils import Q


class QuerySet(models.QuerySet):
    def search(self, query=None):
        query_set = self
        if query is not None:
            or_lookup = (Q(name__icontains=query) |
                         Q(phone__icontains=query)
                         )
            query_set = query_set.filter(or_lookup).distinct()
        return query_set


class GlobalSearchManager(models.Manager):
    def get_queryset(self):
        return QuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class User(models.Model):
    # MY USER
    name = models.CharField(null=False, blank=False, max_length=250)
    password = models.CharField(null=True, blank=False, max_length=250)
    phone = models.PositiveIntegerField(
        null=False, blank=False, unique=True, validators=[MinValueValidator(100000), MaxValueValidator(99999999999)])
    email = models.EmailField(null=True, max_length=250)

    objects = GlobalSearchManager()

    def __str__(self):
        return self.name + " | " + str(self.phone)


class UserContact(models.Model):
    # Contacts that are imported from MY CONTACT LIST
    name = models.CharField(null=True, blank=False, max_length=250)
    # phone = PhoneNumberField(null=True, blank=False)
    phone = models.PositiveIntegerField(
        null=True, blank=False, unique=True, validators=[MinValueValidator(100000), MaxValueValidator(99999999999)])
    email = models.EmailField(null=True, blank=True, max_length=250)
    spam_liklihood = models.IntegerField(null=True, default=0)
    imported_from = models.ForeignKey(
        to=User, on_delete=models.CASCADE, null=True, blank=True)

    objects = GlobalSearchManager()

    def __str__(self):
        return self.name + " | " + str(self.phone) + " | " + str(self.spam_liklihood) + " %"
