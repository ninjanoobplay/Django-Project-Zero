from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import CustomUser
# Register your models here.
admin.site.register(CustomUser, auth_admin.UserAdmin)