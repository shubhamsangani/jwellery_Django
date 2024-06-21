from django.contrib import admin
from .models import *

class UsersAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_name', 'user_email', 'user_phone_no','user_password', 'user_is_active', 'user_created_at']

admin.site.register(Users, UsersAdmin)
