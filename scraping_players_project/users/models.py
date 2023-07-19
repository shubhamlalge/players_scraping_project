from django.core.validators import MinLengthValidator,MaxLengthValidator
from django.db import models

from django.contrib.auth.models import User


class User(User):
    '''Custom user model representing user in the scraping players app'''

    phone_number = models.CharField(max_length=20, unique=True, blank=False, validators=[MinLengthValidator(10)])
    street = models.CharField(max_length=20, null=False, blank=False)
    zip_code = models.IntegerField(null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    state = models.CharField(max_length=100, null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)
    date_of_birth = models.DateField(blank=False, null=False)

    groups = None
    user_permissions = None


