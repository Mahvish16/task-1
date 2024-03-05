from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class AccountsInline(admin.StackedInline):
    model=Accounts
    can_delete=False
    verbose_name_plural='Accounts'
class CustomizedUserAdmin(UserAdmin):
    inlines=(AccountsInline,)
admin.site.unregister(User)
admin.site.register(User,CustomizedUserAdmin)