from django.db import models
import datetime
from django.utils import timezone


class Users(models.Model):

    class Meta:
        db_table = "Users_information_tb"

    user_id = models.CharField(max_length= 60, primary_key=True,default=None)
    user_name = models.CharField(max_length= 100,blank=True, null=True, default= None)
    user_email = models.CharField(max_length= 100,blank=True, null=True, default= None)
    user_phone_no = models.CharField(max_length= 100,blank=True, null=True, default= None)
    user_password = models.CharField(max_length=128)
    forget_password_token = models.CharField(max_length=100,default='')
    user_is_active = models.CharField(max_length= 100, default = True)
    user_created_at = models.DateTimeField(auto_now_add=True)







