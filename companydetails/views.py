from django.shortcuts import render
from products.models import *
from shipping.models import *

def contactUs(request):
    brand_data = brand.objects.all()
    category_data = item_category.objects.all()
    main_category_data = main_category.objects.all()
    user_id = request.session.get('user_id')

    if user_id:
        cart_data = cart_item.objects.filter(user_fk_id=user_id)
        wishlist_data = wishlist_items.objects.all()
        no_of_products_in_cart=len(cart_data)  
        no_of_products_in_wishlist=len(wishlist_data)
    else:
        cart_data=[]
        wishlist_data=[]
        no_of_products_in_cart=0
        no_of_products_in_wishlist=0

    context={
        'brand_data':brand_data,
        'category_data':category_data,
        'main_category_data':main_category_data,
        'no_of_products_in_cart':no_of_products_in_cart,
        'no_of_products_in_wishlist':no_of_products_in_wishlist,
    }
    return render(request, 'contact-us.html', context)

def aboutUs(request):
    return render(request, 'about-us.html')

