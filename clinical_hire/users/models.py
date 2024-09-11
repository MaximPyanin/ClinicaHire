from django.db import models
from django.core.validators import RegexValidator

class User(models.Model):
    id = models.UUIDField(format='hex_verbose')
    name = models.CharField(allow_blank=False)
    surname = models.CharField(allow_blank=False)
    email = models.EmailField(allow_blank=False)
    mobile_phone = models.CharField(max_length=17,allow_blank=False,validators=RegexValidator(
        regex=r'^\+?\d{10,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    ))
    linkedin = models.URLField(allow_blank=True)
    avatar = models.URLField(allow_blank=True)
    city = models.CharField(allow_blank=False)
    country = models.CharField(allow_blank=False)
    portfolio = models.URLField(allow_blank=True)
    hobby = models.CharField(allow_blank=True)
    expected_salary = models.FloatField
    language = models.
    langlevel = ...


