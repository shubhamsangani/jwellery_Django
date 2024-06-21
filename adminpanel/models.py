from django.db import models
import datetime
from django.utils import timezone


class AdminUsers(models.Model):

    class Meta:
        db_table = "admin_users_information_tb"

    admin_user_id = models.CharField(max_length= 60, default= None, primary_key=True)
    admin_user_name = models.CharField(max_length= 100,blank=True, null=True, default= None)
    admin_user_email = models.CharField(max_length= 100,blank=True, null=True, default= None)
    admin_user_phone_no = models.CharField(max_length= 100,blank=True, null=True, default= None)
    admin_user_password = models.CharField(max_length=128, default= None)
    admin_user_is_active = models.CharField(max_length= 100, default = True)
    admin_user_created_at = models.DateTimeField(auto_now_add=True)