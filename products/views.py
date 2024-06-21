from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse,HttpResponse
from .models import *
from shipping.models import *
import uuid
from functools import reduce


def home(request):
    product_brand_item_data = product_brand_item.objects.all()
    product_main_item_data = product_main_item.objects.all()
    image_data = product_image.objects.all()
    products_data = product.objects.all()
    brand_data = brand.objects.all()
    category_data = item_category.objects.all()
    main_category_data = main_category.objects.all()
    cart_data = []
    wishlist_data = []
    no_of_products_in_cart = 0
    no_of_products_in_wishlist = 0
    user_id = request.session.get('user_id')
    if user_id:
        cart_data = cart_item.objects.filter(user_fk_id=user_id)
        wishlist_data = wishlist_items.objects.all()
        no_of_products_in_cart=len(cart_data)  
        no_of_products_in_wishlist=len(wishlist_data)
    
    context = {
    'product_brand_item_data': product_brand_item_data,
    'brand_data': brand_data,
    'category_data': category_data,
    'product_main_item_data' : product_main_item_data,
    'image_data': image_data,
    'products_data':products_data,
    'main_category_data':main_category_data,
    'no_of_products_in_wishlist': no_of_products_in_wishlist,
    'no_of_products_in_cart':no_of_products_in_cart,
    }
    return render(request, "home.html",context)

def compare(request):
    return render(request, "compare.html")

def shop(request, category_name=None, item_category_name=None, brand_name=None):

    brand_data = brand.objects.all()
    main_category_data= main_category.objects.all()
    color_data = product_color.objects.all()
    image_data = product_image.objects.all()
    price_data = product_price.objects.all()
    category_data = item_category.objects.all()
    product_brand_data = product_brand.objects.all()
    size_data = product_size.objects.all()
    cart_data = []
    wishlist_data = []
    no_of_products_in_cart = 0
    no_of_products_in_wishlist = 0
    user_id = request.session.get('user_id')
    if user_id:
        cart_data = cart_item.objects.filter(user_fk_id=user_id)
        wishlist_data = wishlist_items.objects.all()
        no_of_products_in_cart=len(cart_data)  
        no_of_products_in_wishlist=len(wishlist_data)

    size_unique_values = set()
    for i in size_data:
        size_unique_values.add(i.size_value)
    unique_size_values = sorted(size_unique_values)
    color_unique_values = set()
    for i in color_data:
        color_unique_values.add(i.color_name)
    unique_color_values = sorted(color_unique_values)


    if category_name:
        main_category_objects = get_object_or_404(main_category,main_category_name=category_name)
        print('hello world',main_category_objects)
        products_data  = product.objects.filter(product_main__main_fk=main_category_objects)
        context = {'products_data':products_data,
                    'brand_data':brand_data,
                    'color_data':color_data,
                    'image_data':image_data,
                    'price_data':price_data,
                    'size_data':size_data,
                    'main_category_data': main_category_data,
                    'category_data':category_data,
                    'unique_color_values':unique_color_values,
                    'unique_size_values':unique_size_values,
                    'no_of_products_in_wishlist': no_of_products_in_wishlist,
                    'no_of_products_in_cart':no_of_products_in_cart,
                    }
        return render(request, "shop.html", context)

    if item_category_name:
        item_category_objects = get_object_or_404(item_category,item_category_name=item_category_name)
        products_data = product.objects.filter(product_item__item_fk=item_category_objects)
        context = {'products_data':products_data,
                    'brand_data':brand_data,
                    'color_data':color_data,
                    'image_data':image_data,
                    'price_data':price_data,
                    'size_data':size_data,
                    'category_data':category_data,
                    'unique_color_values':unique_color_values,
                    'unique_size_values':unique_size_values,
                    'main_category_data': main_category_data,
                    'no_of_products_in_wishlist': no_of_products_in_wishlist,
                    'no_of_products_in_cart':no_of_products_in_cart,
                    }
        return render(request, "shop.html", context)
    
    if brand_name:
        brand_name_objects = get_object_or_404(brand,brand_name=brand_name)
        products_data = product.objects.filter(product_brand__brand_fk=brand_name_objects)
        context = {'products_data':products_data,
                    'brand_data':brand_data,
                    'color_data':color_data,
                    'image_data':image_data,
                    'price_data':price_data,
                    'size_data':size_data,
                    'category_data':category_data,
                    'unique_color_values':unique_color_values,
                    'unique_size_values':unique_size_values,
                    'main_category_data': main_category_data,
                    'no_of_products_in_wishlist': no_of_products_in_wishlist,
                    'no_of_products_in_cart':no_of_products_in_cart,
                    }
        return render(request, "shop.html", context)
    
    if not (category_name or item_category_name or brand_name):
        products_data = product.objects.all()
        context = {'products_data':products_data,
                    'brand_data':brand_data,
                    'color_data':color_data,
                    'image_data':image_data,
                    'price_data':price_data,
                    'size_data':size_data,
                    'category_data':category_data,
                    'product_brand_data':product_brand_data,
                    'unique_color_values':unique_color_values,
                    'unique_size_values':unique_size_values,
                    'main_category_data': main_category_data,
                    'no_of_products_in_wishlist': no_of_products_in_wishlist,
                    'no_of_products_in_cart':no_of_products_in_cart,
                    }
        return render(request, "shop.html", context)

def productDetails(request,product_id=None):
    products_data = get_object_or_404(product, product_id=product_id)
    product_images = product_image.objects.filter(product_fk=product_id)
    product_brand_data = product_brand.objects.filter(product_fk__product_id=product_id)
    product_size_data = product_size.objects.filter(product_fk__product_id=product_id)
    color_data = product_color.objects.filter(product_fk__product_id=product_id)
    cart_data = []
    wishlist_data = []
    no_of_products_in_cart = 0
    no_of_products_in_wishlist = 0
    user_id = request.session.get('user_id')
    if user_id:
        cart_data = cart_item.objects.filter(user_fk_id=user_id)
        wishlist_data = wishlist_items.objects.all()
        no_of_products_in_cart=len(cart_data)  
        no_of_products_in_wishlist=len(wishlist_data)
    context = {
        'products_data':products_data,
        'product_images':product_images,
        'product_brand_data':product_brand_data[0],
        'product_size_data':product_size_data,
        'color_data':color_data,
        'no_of_products_in_wishlist': no_of_products_in_wishlist,
        'no_of_products_in_cart':no_of_products_in_cart,
    }

    return render(request, "productDetails.html",context)

def wishlist(request):
    cart_data = []
    wishlist_data = []
    no_of_products_in_cart = 0
    no_of_products_in_wishlist = 0
    user_id = request.session.get('user_id')
    if user_id:
        cart_data = cart_item.objects.filter(user_fk_id=user_id)
        wishlist_data = wishlist_items.objects.all()
        no_of_products_in_cart=len(cart_data)  
        no_of_products_in_wishlist=len(wishlist_data)
    brand_data = brand.objects.all()
    category_data = item_category.objects.all()
    main_category_data = main_category.objects.all()
    context={'wishlist_data':wishlist_data, 
                            "no_of_products_in_wishlist": no_of_products_in_wishlist,
                            "no_of_products_in_cart":no_of_products_in_cart, 
                            "brand_data":brand_data,  
                            "category_data": category_data,  
                            "main_category_data":main_category_data,                                      
                                            }
    return render(request, "wishlist.html", context)

def wishlistdelete(request,wishlist_item_id):
    item = wishlist_items.objects.get(wishlist_item_id=wishlist_item_id)
    print(item)
    item.delete()
    return redirect('wishlistPage')

def filter_product(request):
    if request.method == 'POST':
        filter_brand_id = request.POST.getlist('brand[]')
        filter_color_id = request.POST.getlist('color[]')
        filter_size_id = request.POST.getlist('size[]')
        filter_category_id = request.POST.getlist('category[]')
    
        # Start with all products
        products_data = product.objects.all()
        
        # Apply filters based on selected brand IDs
        if filter_brand_id:
            brand_product_ids = set(product_brand.objects.filter(brand_fk_id__in=filter_brand_id).values_list('product_fk', flat=True))
            products_data = products_data.filter(product_id__in=brand_product_ids)
        
        # Apply filters based on selected color IDs
        if filter_color_id:
            color_product_ids = set(product_color.objects.filter(color_name__in=filter_color_id).values_list('product_fk', flat=True))
            products_data = products_data.filter(product_id__in=color_product_ids)
        
        # Apply filters based on selected size IDs
        if filter_size_id:
            size_product_ids = set(product_size.objects.filter(size_value__in=filter_size_id).values_list('product_fk', flat=True))
            products_data = products_data.filter(product_id__in=size_product_ids)
        
        # Apply filters based on selected category IDs
        if filter_category_id:
            category_product_ids = set(product_item.objects.filter(item_fk__item_category_name__in=filter_category_id).values_list('product_fk', flat=True))
            products_data = products_data.filter(product_id__in=category_product_ids)
        
        # Prepare product data to be returned in the response
        product_data = []
        for productt in products_data:
            pro_img = product_image.objects.filter(product_fk=productt.product_id).first()
            brand_name = product_brand.objects.filter(product_fk=productt.product_id).first().brand_fk.brand_name
            product_data.append({
                "product_discount": productt.product_discount,
                "product_id": productt.product_id,
                "product_name": productt.product_name,
                "brand_name": brand_name,
                "product_price": productt.product_price,
                "product_image": pro_img.image_path if pro_img else None,
            })
        
        # Return filtered product data as JSON response
        response_data = {
            "msg": "success",
            "data": product_data
        }
        return JsonResponse(response_data)


def addtowishlist(request,product_id):
    wishlist_item_id = str(uuid.uuid1())
    user_id = request.session.get('user_id')
    try:
        current_user = Users.objects.get(user_id=user_id)
    except Users.DoesNotExist:
        return HttpResponse('User does not exist or is not logged')
    product_data = product.objects.get(product_id = product_id)
    image_data = product_image.objects.get(product_fk__product_id=product_id)
    price_data = product_price.objects.get(product_fk__product_id=product_id)  

    if wishlist_items.objects.filter(user_fk=current_user, product_fk=product_data).exists():
        return redirect('homePage')
    else:
        new_wishlist_item = wishlist_items(
            wishlist_item_id=wishlist_item_id,
            user_fk=current_user,
            product_fk=product_data,
            product_image_fk=image_data,
            product_price_fk=price_data
        )
        new_wishlist_item.save()
    return redirect('shopPage')
    
def search_view(request):
    query = request.GET.get('query')
    cart_data = []
    wishlist_data = []
    no_of_products_in_cart = 0
    no_of_products_in_wishlist = 0
    user_id = request.session.get('user_id')
    if user_id:
        cart_data = cart_item.objects.filter(user_fk_id=user_id)
        wishlist_data = wishlist_items.objects.all()
        no_of_products_in_cart=len(cart_data)  
        no_of_products_in_wishlist=len(wishlist_data)
    brand_data = brand.objects.all()
    category_data = item_category.objects.all()
    main_category_data = main_category.objects.all()

    productss = []
    if query:
        productss = product.objects.filter(product_name__icontains=query)
    print(productss)
    context={
        'query': query, 
        'productss': productss,
        'no_of_products_in_cart': no_of_products_in_cart,
        'no_of_products_in_wishlist': no_of_products_in_wishlist,
        'brand_data': brand_data,
        'category_data': category_data,
        'main_category_data':main_category_data,
    }
    return render(request, 'search.html', context)

def addtocart(request,product_id):
    user_id = request.session.get('user_id')
    try:
        current_user = Users.objects.get(user_id=user_id)
    except Users.DoesNotExist:
        return HttpResponse('User does not exist or is not logged')

    existing_cart_item= cart_item.objects.filter(user_fk=current_user, product_fk__product_id=product_id).first()

    if existing_cart_item:
        existing_quanity=int(existing_cart_item.items_quantity)
        existing_cart_item.items_quantity = existing_quanity + 1
        existing_cart_item.save()
    else:        
        cart_items_id = str(uuid.uuid1())
        product_data = product.objects.get(product_id = product_id)
        image_data = product_image.objects.get(product_fk__product_id=product_id)
        price_data = product_price.objects.get(product_fk__product_id=product_id)
        item_quantity = 1

        new_cart_item = cart_item(
            cart_items_id=cart_items_id,
            user_fk=current_user,
            product_fk=product_data,
            product_image_fk=image_data,
            items_quantity=item_quantity,
            product_price_fk=price_data
        )
        new_cart_item.save()

    return redirect('shopPage')