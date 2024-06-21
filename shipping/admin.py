from django.contrib import admin
from .models import *

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart_items_id', 'user_fk', 'product_fk', 'product_image_fk', 'items_quantity','product_price_fk']

class AddressAdmin(admin.ModelAdmin):
    list_display = ('address_id', 'house_no', 'residence_name', 'landmark', 'city', 'pin_code', 'state', 'country', 'deliver_to_whom', 'deliver_to_contact', 'user_fk')

class ShippingAdmin(admin.ModelAdmin):
    list_display = ['shipping_id', 'cart_fk', 'user_fk', 'address_fk']

admin.site.register(cart_item, CartItemAdmin)
admin.site.register(address, AddressAdmin)
admin.site.register(shipping, ShippingAdmin)
