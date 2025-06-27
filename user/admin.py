from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

@admin.register(models.User)
class UserAdmin(UserAdmin):
    model = models.User
    list_display = ('id', 'username', 'email',  'is_superuser','is_staff', 'is_active','phone_number')
    