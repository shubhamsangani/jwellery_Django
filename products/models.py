from django.db import models
from users.models import *
import datetime

class main_category(models.Model):

    class Meta:
        db_table = "Main_Category_information_tb"

    main_category_id = models.CharField(max_length= 60, primary_key=True)
    main_category_name = models.CharField(max_length= 100,blank=True, null=True, default= None)
    main_category_is_active = models.CharField(max_length= 100,default = True)
    main_category_created_at = models.DateTimeField(auto_now_add = True)

class brand(models.Model):

    class Meta:
        db_table = "Brand_information_tb"

    brand_id = models.CharField(max_length= 60, primary_key=True)
    brand_name = models.CharField(max_length= 100,blank=True, null=True, default= None)
    brand_is_active = models.CharField(max_length= 100, default = True)
    brand_created_at = models.DateTimeField(auto_now_add = True)

class item_category(models.Model):

    class Meta:
        db_table = "Item_Category_information_tb"

    item_category_id = models.CharField(max_length= 60, primary_key=True)
    item_category_name = models.CharField(max_length= 100,blank=True, null=True, default= None)
    item_category_is_active = models.CharField(max_length= 100, default = True)
    item_category_created_at = models.DateTimeField(auto_now_add = True)

class product(models.Model):
    class Meta:
        db_table = "Product_information_tb"

    product_id = models.CharField(max_length= 60, primary_key=True)
    product_name = models.CharField(max_length= 100,blank=True, null=True, default= None)
    product_description = models.CharField(max_length= 10000,blank=True, null=True, default= None)
    product_price = models.CharField(max_length= 100,blank=True, null=True, default= None)
    product_stock= models.CharField(max_length= 100,blank=True, null=True, default= None)
    product_discount = models.CharField(max_length= 100,blank=True, null=True, default= None)
    product_is_active = models.CharField(max_length= 100, default = True)
    product_created_at = models.DateTimeField(auto_now_add = True)
    product_is_featured = models.CharField(max_length= 100, default = False)
    
    @property
    def product_discounted_price(self):
        if self.product_discount:
            try:
                price = float(self.product_price)
                discount = float(self.product_discount)
                discounted_price = price - (price * discount / 100)
                return discounted_price
            except ValueError:
                return None
        else:
            return None

class main_brand(models.Model):

    class Meta:
        db_table = "main_brand_information_tb"
    
    main_brand_id = models.CharField(max_length= 60, primary_key=True)
    main_fk = models.ForeignKey(main_category, on_delete=models.CASCADE)
    brand_fk = models.ForeignKey(brand, on_delete=models.CASCADE)

class main_item(models.Model):

    class Meta:
        db_table = "main_item_information_tb"
    
    main_item_id = models.CharField(max_length= 60, primary_key=True)
    main_fk = models.ForeignKey(main_category, on_delete=models.CASCADE)
    item_fk = models.ForeignKey(item_category, on_delete=models.CASCADE)
    
class brand_item(models.Model):

    class Meta:
        db_table = "brand_item_information_tb"
    
    brand_item_id = models.CharField(max_length= 60, primary_key=True)
    brand_fk = models.ForeignKey(brand, on_delete=models.CASCADE)
    item_fk = models.ForeignKey(item_category, on_delete=models.CASCADE)

class product_main(models.Model):

    class Meta:
        db_table = "product_main_information_tb"
    
    product_main_id = models.CharField(max_length= 60, primary_key=True)
    product_fk = models.ForeignKey(product, on_delete=models.CASCADE)
    main_fk = models.ForeignKey(main_category, on_delete=models.CASCADE)

class product_main_brand(models.Model):

    class Meta:
        db_table = "product_main_brand_information_tb"
    
    product_main_brand_id = models.CharField(max_length= 60, primary_key=True)
    main_brand_fk = models.ForeignKey(main_brand, on_delete=models.CASCADE)
    product_fk = models.ForeignKey(product, on_delete=models.CASCADE)

class product_item(models.Model):

    class Meta:
        db_table = "product_item_information_tb"
    
    product_item_id = models.CharField(max_length= 60, primary_key=True)
    product_fk = models.ForeignKey(product, on_delete=models.CASCADE)
    item_fk = models.ForeignKey(item_category, on_delete=models.CASCADE)

class product_main_item(models.Model):

    class Meta:
        db_table = "product_main_item_information_tb"
    
    product_main_item_id = models.CharField(max_length= 60, primary_key=True)
    product_fk = models.ForeignKey(product, on_delete=models.CASCADE)
    main_item_fk = models.ForeignKey(main_item, on_delete=models.CASCADE)

class product_brand(models.Model):

    class Meta:
        db_table = "product_brand_information_tb"
    
    product_brand_id = models.CharField(max_length= 60, primary_key=True)
    product_fk = models.ForeignKey(product, on_delete=models.CASCADE)
    brand_fk = models.ForeignKey(brand, on_delete=models.CASCADE)

class product_brand_item(models.Model):

    class Meta:
        db_table = "product_brand_item_information_tb"
    
    product_brand_item_id = models.CharField(max_length= 60, primary_key=True)
    product_fk = models.ForeignKey(product, on_delete=models.CASCADE)
    brand_item_fk = models.ForeignKey(brand_item, on_delete=models.CASCADE)

class product_image(models.Model):

    class Meta:
        db_table = "product_image_information_tb"
    
    product_image_id = models.CharField(max_length= 60, primary_key=True)
    image_path = models.CharField(max_length= 100, default = True)
    product_image_is_active = models.CharField(max_length= 100, default = True)
    product_image_created_at = models.DateTimeField(auto_now_add = True)
    product_fk = models.ForeignKey(product, on_delete=models.CASCADE)

class product_size(models.Model):

    class Meta:
        db_table = "product_size_information_tb"
    
    product_size_id = models.CharField(max_length= 60, primary_key=True)
    size_value = models.CharField(max_length= 100,blank=True, null=True, default= None)
    product_size_is_active = models.CharField(max_length=100, default = True)
    product_size_created_at = models.DateTimeField(auto_now_add = True)
    product_fk = models.ForeignKey(product, on_delete=models.CASCADE)

class product_color(models.Model):

    class Meta:
        db_table = "product_color_information_tb"
    
    product_color_id = models.CharField(max_length= 60, primary_key=True)
    color_stock = models.CharField(max_length= 100,blank=True, null=True, default= None)
    color_name = models.CharField(max_length= 100,blank=True, null=True, default= None)
    product_color_is_active = models.CharField(max_length=100, default = True)
    product_color_created_at = models.DateTimeField(auto_now_add = True)
    product_fk = models.ForeignKey(product, on_delete=models.CASCADE)

class product_size_color(models.Model):

    class Meta:
        db_table = "product_size_color_information_tb"
    
    product_size_color_id = models.CharField(max_length= 60, primary_key=True)
    color_fk = models.ForeignKey(product_color, on_delete=models.CASCADE)
    size_fk = models.ForeignKey(product_size, on_delete=models.CASCADE)
    product_fk = models.ForeignKey(product, on_delete=models.CASCADE)

class product_price(models.Model):
    
    class Meta:
        db_table = "product_price_information_tb"
    
    product_price_id = models.CharField(max_length= 60, primary_key=True)
    product_price = models.CharField(max_length=100,blank=True, null=True, default= None)
    extra_charges = models.CharField(max_length=100,blank=True, null=True, default= None)
    final_charges = models.CharField(max_length=100,blank=True, null=True, default= None)
    product_fk = models.ForeignKey(product, on_delete=models.CASCADE, related_name='product_prices')
    size_fk = models.ForeignKey(product_size, on_delete=models.CASCADE)
    color_fk = models.ForeignKey(product_color, on_delete=models.CASCADE)
    product_price_is_active = models.CharField(max_length=100, default = True)
    product_price_created_at = models.DateTimeField(auto_now_add = True)

class wishlist_items(models.Model):
    
    class Meta:
        db_table = "wishlist_items_information_tb"
    
    wishlist_item_id = models.CharField(max_length= 60, primary_key=True)
    user_fk = models.ForeignKey(Users,on_delete=models.CASCADE, default=None)
    product_fk = models.ForeignKey(product, on_delete=models.CASCADE)
    product_image_fk = models.ForeignKey(product_image,on_delete=models.CASCADE)
    product_price_fk = models.ForeignKey(product_price,on_delete=models.CASCADE)




