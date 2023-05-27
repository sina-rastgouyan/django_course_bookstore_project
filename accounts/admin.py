from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age', )}),
    )

    list_display = ['username', 'email', 'age', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)

