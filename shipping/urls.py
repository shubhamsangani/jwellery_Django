from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cartPage'),
    path('checkout/', views.checkout, name='checkoutPage'),
    path('delete/<uuid:cart_items_id>',views.cartdelete, name='itemDeletePage'),
    path('quantity_update/', views.quantity_update, name='quantity_updatePage'),
    path('address_form_view/', views.address_form_view, name="address_Form_SubmitPage"),
    path('payment_successful/', views.payment_successful, name='payment_successful'),
    path('payment_cancelled/', views.payment_cancelled, name='payment_cancelled'),
    path('payment/', views.create_checkout_session, name='create_checkout_session'),
]