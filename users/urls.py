from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('loginregister', views.LoginRegister, name='loginRegisterPage'),
    path('myaccount', views.myAccount, name='myAccountPage'),
    path('forget-password/' , views.ForgetPassword , name="forget_password"),
    path('change-password/<uuid:token>/', views.ChangePassword, name="change_password"),
    path('logout/', views.logout, name='logout'),  
    path('add-address/' , views.AddAddress , name="add_address"),
    path('add-address-submit/' , views.address_form_view , name="addressSubmitPage"),
    path('address-edit-page/<str:address_id>/' , views.address_edit , name="AddressEditPage"),
    path('edit-address/' , views.EditAddress , name="EditAddressPage"),
   ]