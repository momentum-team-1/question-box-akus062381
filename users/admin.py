from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import User
from core.forms import MyUserCreationForm, MyUserChangeForm

class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = User
    list_display = ['username', 'image', 'current_city', 'bio']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('image', 'current_city', 'bio')}),
    )


admin.site.register(User, MyUserAdmin)

