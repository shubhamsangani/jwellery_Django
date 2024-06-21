from django.contrib import admin
from .models import *

class UsersAdmin(admin.ModelAdmin):
    list_display = ['admin_user_id', 'admin_user_name', 'admin_user_email', 'admin_user_phone_no','admin_user_password', 'admin_user_is_active', 'admin_user_created_at']

admin.site.register(AdminUsers, UsersAdmin)