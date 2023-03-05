from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=32, blank=True, null=True)  # new
    address = models.CharField(max_length=64, blank=True, null=True)  # new
    code = models.IntegerField(null=True)

    class Meta:
        db_table = "Cutom_user"
