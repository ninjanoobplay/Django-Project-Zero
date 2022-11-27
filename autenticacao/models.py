from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class CustomUser(AbstractUser):
    ddd = models.IntegerField(default='0',blank=False)
    phone= models.IntegerField(default='0',blank=False)

    class Meta:
        verbose_name = 'User'