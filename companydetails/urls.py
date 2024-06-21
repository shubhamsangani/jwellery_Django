from django.urls import path
from . import views

urlpatterns = [
    path('contactus/', views.contactUs, name='contactUsPage'),
    path('aboutus/', views.aboutUs, name='aboutUsPage'),
]