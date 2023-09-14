from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomCreationUserForm, CustomChangeUserForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomCreationUserForm
    form = CustomChangeUserForm
    list_display = ['email', 'username']


