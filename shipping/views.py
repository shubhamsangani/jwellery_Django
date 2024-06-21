from django.shortcuts import render, redirect
import json
from django.http import JsonResponse
from django.urls import reverse
from .models import *
from products.models import *
from users.models import Users
import stripe
import uuid

def cart(request):
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

    context={'cart_data': cart_data, 
            'no_of_products_in_wishlist': no_of_products_in_wishlist,
            'no_of_products_in_cart':no_of_products_in_cart,
            "brand_data":brand_data,  
            "category_data": category_data,  
            "main_category_data":main_category_data,}

    return render(request, 'cart.html', context)

def cartdelete(request, cart_items_id):
    item = cart_item.objects.get(cart_items_id=cart_items_id)
    print(item)
    item.delete()
    return redirect('cartPage')

def checkout(request):
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
        user_addresses = address.objects.filter(user_fk=user_id)

    subtotal = request.GET.get('subtotal')
    total = request.GET.get('total')
    request.session['total'] = total
    request.session['subtotal'] = subtotal

    context = {
        "cart_items": cart_data,
        "subtotal": subtotal,
        "total": total,
        "brand_data": brand_data,
        "category_data": category_data,
        "main_category_data":main_category_data,
        'no_of_products_in_wishlist': no_of_products_in_wishlist,
        'no_of_products_in_cart':no_of_products_in_cart,
        "user_addresses": user_addresses,
    }
    return render(request, 'checkout.html', context)

def quantity_update(request):
    if request.method=='POST':
        user_id = request.session.get('user_id')
        data= json.loads(request.body)
        product_id=data['productId']
        quantity=data['quantity']
        try:
            cart_item_instance = cart_item.objects.get(product_fk_id=product_id, user_fk_id=user_id)
        except  Exception as e:
            print(e)
            return JsonResponse({'status': 'error', 'message': 'Cart item not found'}, status=404)
            
        # Update the items_quantity field with the new quantity
        cart_item_instance.items_quantity = quantity
        cart_item_instance.save()
            
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

def address_form_view(request):
    if request.method == 'POST':
        # Check if the checkbox is checked
        ship_to_different = request.POST.get('ship_to_different',None)
        # Get the user ID from the session
        user_id = request.session.get("user_id")
        # Retrieve the user instance from the database
        user_instance = Users.objects.get(user_id=user_id)
        # If ship_to_different is checked, retrieve values for secondary address
        if ship_to_different == '0':
            f_name_2 = request.POST.get('f_name_2')
            l_name_2 = request.POST.get('l_name_2')
            email_2 = request.POST.get('email_2')
            country_2 = request.POST.get('country_2')
            street_address_2 = request.POST.get('street_address_2')
            town_2 = request.POST.get('town_2')
            state_2 = request.POST.get('state_2')
            postcode_2 = request.POST.get('postcode_2')
            # Set fields for primary address to None
            house_no = None
            residence_name = None
            landmark = None
            city = None
            pin_code = None
            state = None
            country = None
            deliver_to_whom = None
            deliver_to_contact = None
        else:
            # If ship_to_different is not checked, retrieve values for primary address
            house_no = request.POST.get('house_no')
            residence_name = request.POST.get('residence_name')
            landmark = request.POST.get('landmark')
            city = request.POST.get('city')
            pin_code = request.POST.get('pin_code')
            state = request.POST.get('state')
            country = request.POST.get('country')
            deliver_to_whom = request.POST.get('deliver_to_whom')
            deliver_to_contact = request.POST.get('deliver_to_contact')
            # Set fields for secondary address to None
            f_name_2 = None
            l_name_2 = None
            email_2 = None
            country_2 = None
            street_address_2 = None
            town_2 = None
            state_2 = None
            postcode_2 = None
        # Create a new address instance with the retrieved values
        new_address = address.objects.create(
            address_id=str(uuid.uuid4()),  # Generate a unique address ID
            house_no=house_no,
            user_fk=user_instance,
            residence_name=residence_name,
            city=city,
            pin_code=pin_code,
            state=state,
            country=country,
            deliver_to_whom=deliver_to_whom,
            deliver_to_contact=deliver_to_contact,
            landmark=landmark,
            ship_to_different=ship_to_different,
            f_name_2=f_name_2,
            l_name_2=l_name_2,
            email_2=email_2,
            country_2=country_2,
            street_address_2=street_address_2,
            town_2=town_2,
            state_2=state_2,
            postcode_2=postcode_2,
        )
        # Save the new address instance
        new_address.save()
        # Get all addresses for the user
        user_addresses = address.objects.filter(user_fk=user_instance)
        # Display a success message
        success_message = 'Address saved successfully!'
        # Render the checkout page with the success message and user addresses
        return render(request, 'checkout.html', {'success_message': success_message, 'user_addresses': user_addresses})
    # If the request method is not POST, render the checkout.html template
    return render(request, 'checkout.html')

def payment_successful(request):
    user_id = request.session.get('user_id')
    total = request.session.get('total')
    subtotal = request.session.get('subtotal')
    if user_id:
        # Query cart items for the current user
        cart_items = cart_item.objects.filter(user_fk_id=user_id)

    context={
        "cart_items": cart_items,
        'total':total,
        "subtotal": subtotal,
    }
    return render(request,'success.html', context)

def payment_cancelled(request):
    return render(request,'cancel.html')
    
def create_checkout_session(request):
    if request.method == 'POST':
        cart_data = None
        user_id = request.session.get('user_id')
        if user_id:
            # Query cart items for the current user
            cart_data = cart_item.objects.filter(user_fk_id=user_id)
        line_items = []  # Initialize line_items list
        for item in cart_data:  # Change the loop variable name
            product = item.product_fk
            product_fk = item.product_price_fk
            line_item = {
                'price_data': {
                    'currency': 'inr',
                    'unit_amount': int(float(product_fk.final_charges) * 100),
                    'product_data': {
                    'name': product.product_name,
                    },
                },
                'quantity': item.items_quantity,
            }
            line_items.append(line_item)        # Create a Stripe checkout session
        stripe.api_key = 'sk_test_51P6RQPSH7gQtXoiNSE95fMfwwAbkkxR7kvzpxe8DKR6nKboXb12mYULmtbx6lxADFjHTXk0uBfVqGjgNBlOMI5OI00t9r3vDDJ'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=request.build_absolute_uri(reverse('payment_successful')),
            cancel_url=request.build_absolute_uri(reverse('payment_cancelled')),
            # Add other parameters as needed
        )
        # Redirect the user to the Stripe checkout page
        return redirect(checkout_session.url)
    else:
            # Handle GET requests or other HTTP methods
            # Return an error response or redirect to an appropriate page
        pass