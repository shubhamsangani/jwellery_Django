from django.db import models
from users.models import *
from products.models import *
import datetime

class cart_item(models.Model):
    class Meta:
        db_table = "cart_items_information_tb"
    cart_items_id = models.CharField(max_length= 60, primary_key=True, default=None)
    user_fk = models.ForeignKey(Users,on_delete=models.CASCADE, default=None)
    product_fk = models.ForeignKey(product,on_delete=models.CASCADE, default=None)
    product_image_fk = models.ForeignKey(product_image,on_delete=models.CASCADE, default=None)
    items_quantity = models.CharField(max_length= 60, default=None)
    product_price_fk = models.ForeignKey(product_price,on_delete=models.CASCADE, default=None)
    cart_created_at = models.DateTimeField(auto_now_add = True)

class address(models.Model):
    class Meta:
        db_table = "address_information_tb"
    address_id= models.CharField(max_length=60, primary_key=True)
    house_no = models.CharField(max_length= 10000,blank=True, null=True, default= None)
    residence_name = models.CharField(max_length= 10000,blank=True, null=True, default= None)
    landmark = models.CharField(max_length= 10000,blank=True, null=True, default= None)
    city = models.CharField(max_length= 10000,blank=True, null=True, default= None)
    pin_code = models.CharField(max_length= 10000,blank=True, null=True, default= None)
    state = models.CharField(max_length= 10000,blank=True, null=True, default= None)
    country = models.CharField(max_length= 10000,blank=True, null=True, default= None)
    deliver_to_whom = models.CharField(max_length= 10000,blank=True, null=True, default= None)
    deliver_to_contact = models.CharField(max_length= 10000,blank=True, null=True, default= None)
    user_fk = models.ForeignKey(Users, on_delete=models.CASCADE)

class shipping(models.Model):

    class Meta:
        db_table = "shipping_information_tb"

    shipping_id = models.CharField(max_length= 60, primary_key=True, default=None)
    cart_fk = models.ForeignKey(cart_item, on_delete=models.CASCADE, default=None)
    user_fk = models.ForeignKey(Users, on_delete=models.CASCADE, default=None)
    address_fk = models.ForeignKey(address, on_delete=models.CASCADE, default=None)

