from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_employee = models.BooleanField('Is employee', default=False)
    is_cfo = models.BooleanField('Is cfo', default=False)
    is_accountant = models.BooleanField('Is accountant', default=False)
    is_vendor = models.BooleanField('Is vendor', default=False)
    is_manager = models.BooleanField('Is manager', default=False)
    