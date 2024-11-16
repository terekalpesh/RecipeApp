from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Recipe, Category
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'username',
        'phone',
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('phone', )}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ("username", 'phone', "usable_password", "password1", "password2", )}),)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Recipe)
admin.site.register(Category)

