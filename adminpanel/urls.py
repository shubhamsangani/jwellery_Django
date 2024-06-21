from django.urls import path
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.AdminLoginRegister, name='adminloginregisterPage'),
    path('adminmyaccount/', views.adminmyaccount, name='adminmyaccountPage'),
    path('addproduct/', views.addproduct, name='addproductPage' ),
    path('viewproduct/', views.product_details, name='viewproductPage' ),
    path('deleteproduct/', views.deletepageview, name='deleteproductPage'),
    path('deleteproduct/<uuid:product_id>/', views.delete_product, name='delete_product'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),  
    ]

