# Register your models here.
from django.contrib import admin
from .models import *

# Register your models here.
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ['main_category_id', 'main_category_name', 'main_category_is_active', 'main_category_created_at']
class BrandAdmin(admin.ModelAdmin):
    list_display = ['brand_id', 'brand_name', 'brand_is_active', 'brand_created_at']

class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ['item_category_id', 'item_category_name', 'item_category_is_active', 'item_category_created_at']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'product_name', 'product_price', 'product_stock','product_discount','product_is_featured','product_is_active', 'product_created_at',]

class MainBrandAdmin(admin.ModelAdmin):
    list_display = ['main_brand_id', 'main_fk', 'brand_fk']

class MainItemAdmin(admin.ModelAdmin):
    list_display = ['main_item_id', 'main_fk', 'item_fk']

class BrandItemAdmin(admin.ModelAdmin):
    list_display = ['brand_item_id', 'brand_fk', 'item_fk']

class ProductMainAdmin(admin.ModelAdmin):
    list_display = ['product_main_id', 'product_fk', 'main_fk']

class ProductMainBrandAdmin(admin.ModelAdmin):
    list_display = ['product_main_brand_id', 'main_brand_fk', 'product_fk']

class ProductItemAdmin(admin.ModelAdmin):
    list_display = ['product_item_id', 'product_fk', 'item_fk']

class ProductMainItemAdmin(admin.ModelAdmin):
    list_display = ['product_main_item_id', 'product_fk', 'main_item_fk']

class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ['product_brand_id', 'product_fk', 'brand_fk']

class ProductBrandItemAdmin(admin.ModelAdmin):
    list_display = ['product_brand_item_id', 'product_fk', 'brand_item_fk']

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product_image_id', 'image_path', 'product_image_is_active', 'product_image_created_at', 'product_fk']

class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ['product_size_id', 'size_value', 'product_size_is_active', 'product_size_created_at', 'product_fk']

class ProductColorAdmin(admin.ModelAdmin):
    list_display = ['product_color_id', 'color_stock', 'color_name', 'product_color_is_active', 'product_color_created_at', 'product_fk']

class ProductSizeColorAdmin(admin.ModelAdmin):
    list_display = ['product_size_color_id', 'color_fk', 'size_fk', 'product_fk']

class ProductPriceAdmin(admin.ModelAdmin):
    list_display = ['product_price_id', 'product_price', 'extra_charges', 'final_charges', 'product_fk', 'size_fk', 'color_fk','product_price_is_active','product_price_created_at']

class WishlistAdmin(admin.ModelAdmin):
    list_display = ['wishlist_item_id','product_fk','product_image_fk','product_price_fk']

admin.site.register(main_category, MainCategoryAdmin)
admin.site.register(brand, BrandAdmin)
admin.site.register(item_category, ItemCategoryAdmin)
admin.site.register(product, ProductAdmin)
admin.site.register(main_brand, MainBrandAdmin)
admin.site.register(main_item, MainItemAdmin)
admin.site.register(brand_item, BrandItemAdmin)
admin.site.register(product_main, ProductMainAdmin)
admin.site.register(product_main_brand, ProductMainBrandAdmin)
admin.site.register(product_item, ProductItemAdmin)
admin.site.register(product_main_item, ProductMainItemAdmin)
admin.site.register(product_brand, ProductBrandAdmin)
admin.site.register(product_brand_item, ProductBrandItemAdmin)
admin.site.register(product_image, ProductImageAdmin)
admin.site.register(product_size, ProductSizeAdmin)
admin.site.register(product_color, ProductColorAdmin)
admin.site.register(product_size_color, ProductSizeColorAdmin)
admin.site.register(product_price, ProductPriceAdmin)
admin.site.register(wishlist_items, WishlistAdmin)