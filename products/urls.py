from django.urls import path
from . import views
from  django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='homePage'),
    path('shop/', views.shop, name='shopPage'),
    path('shop/<str:category_name>/', views.shop, name='shopPageCategory'),
    path('shop/brand/<str:brand_name>/', views.shop, name='shopPageBrand'),
    path('shop/item/<str:item_category_name>/', views.shop, name='shopPageItemCategory'),
    path('product-details/<str:product_id>', views.productDetails, name='productDetailsPage'),
    path('wishlist/', views.wishlist, name='wishlistPage'),
    path('delete/<str:wishlist_item_id>',views.wishlistdelete, name='wishlistDeletePage'),
    path('addtowishlist/<str:product_id>',views.addtowishlist, name='addToWishlistPage'),
    path('addtocart/<str:product_id>',views.addtocart, name='addToCartPage'),
    path('compare/', views.compare, name='comparePage'),
    path('filter-product/', views.filter_product, name='filterProductPage'),
    path('search/', views.search_view, name='search'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)