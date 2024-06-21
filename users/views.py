from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import auth
from django.contrib import messages
from users.models import Users
from products.models import *
from shipping.models import *
import uuid
import random
import string
from .helpers import send_forget_password_mail


def custom_authenticate(username, password):
    try:
        user = Users.objects.get(user_name=username)
        if user.user_password == password:
            return user
    except Users.DoesNotExist:
        return None

def LoginRegister(request):
    brand_data = brand.objects.all()
    category_data = item_category.objects.all()
    main_category_data = main_category.objects.all()
    user_id = request.session.get('user_id')

    cart_data = []
    wishlist_data = []
    no_of_products_in_cart = 0
    no_of_products_in_wishlist = 0

    if user_id:
        cart_data = cart_item.objects.filter(user_fk_id=user_id)
        wishlist_data = wishlist_items.objects.all()
        no_of_products_in_cart=len(cart_data)  
        no_of_products_in_wishlist=len(wishlist_data)

    form_data = {
        'user_name': '',
        'user_email': '',
        'user_phone_number': '',
        'user_password': '',
        'repeat_password': '',
    }

    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        print("Form type:", form_type)  # Debugging
        
        if form_type == 'login':
            username = request.POST.get('login_username')
            password = request.POST.get('login_password')

            # Check if username and password are provided
            if username and password:
                user = custom_authenticate(username, password)
                if user is not None:
                    # Set session or cookie to indicate user is logged in
                    request.session['user_id'] = user.user_id
                    print("User logged in:", user.user_name)
                    return redirect('homePage')  # Redirect to home page after successful login
                else:
                    messages.error(request, "Invalid username or password.")
                    print("Authentication failed for user:", username)
            else:
                messages.error(request, "Username and password are required.")
                print("Authentication failed: Username or password not provided.")

        elif form_type == 'signup':
            form_data['user_name'] = request.POST.get('user_name').strip()
            form_data['user_email'] = request.POST.get('user_email').strip()
            form_data['user_phone_number'] = request.POST.get('user_phone_number').strip()
            form_data['user_password'] = request.POST.get('user_password').strip()
            form_data['repeat_password'] = request.POST.get('repeat_password').strip()

            if any(value == '' for value in form_data.values()):
                messages.error(request, "All fields are required!!")
            else:
                if form_data['user_password'] != form_data['repeat_password']:
                    messages.error(request, "Passwords do not match!!")
                else:
                    randomstr = ''.join(random.choices(string.ascii_lowercase + string.digits, k=15))
                    uniqueID = "BroaderAI_user_information_" + randomstr
                    active = "On"

                    user = Users(
                        user_id=uniqueID,
                        user_name=form_data['user_name'],
                        user_email=form_data['user_email'],
                        user_phone_no=form_data['user_phone_number'],
                        user_password=form_data['user_password'],
                        user_is_active=active,
                    )
                    user.save()

                    if user.user_id:
                        messages.success(request, "User added successfully!!")
                        print("User added successfully:", user.user_name)  # Debugging
                        return redirect('homePage')  # Redirect to the correct URL after successful signup
                    else:
                        messages.error(request, "Something went wrong!!")
                        print("Error: Something went wrong while saving user.")  # Debugging

    return render(request, "loginRegister.html", {'form_data': form_data,
                                                'brand_data': brand_data,
                                                'category_data':category_data,
                                                'main_category_data':main_category_data,
                                                'no_of_products_in_cart':no_of_products_in_cart,
                                                'no_of_products_in_wishlist':no_of_products_in_wishlist,})

def logout(request):
    # Clear the session data
    request.session.clear()
    return redirect('loginRegisterPage')

def ForgetPassword(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            print(username,'sdsssssss')
            if not Users.objects.filter(user_name=username).exists():
                messages.error(request, 'No user found with this username.')
                return redirect('/auth/forget-password/')
            user_obj = Users.objects.get(user_name=username)
            token = str(uuid.uuid4())
            print(token)
            user_obj.forget_password_token = token
            user_obj.save()
            print(user_obj.user_email,'gggggggggggggggggggg')
            # Send forget password email
            send_forget_password_mail(user_obj.user_email, token)
            messages.success(request, 'An email has been sent with password reset instructions.')
            return redirect('loginRegisterPage')
    except Exception as e:
        messages.error(request, str(e))
    return render(request, 'forget-password.html')

def ChangePassword(request, token):
    context = {}
    try:
        user_obj = Users.objects.filter(forget_password_token=token).first()
        if user_obj is None:
            messages.error(request, 'Invalid token.')
            return redirect(f'/auth/change-password/{token}/')
        context['user_id'] = user_obj.user_id
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            if new_password != confirm_password:
                messages.error(request, 'Passwords do not match.')
                return redirect(f'/auth/change-password/{token}/')
            # Update the user's password in the database without hashing
            user_obj.user_password = new_password
            user_obj.save()
            messages.success(request, 'Password changed successfully.')
            return redirect('homePage')
    except Exception as e:
        messages.error(request, str(e))
    return render(request, 'change-password.html', context)

def myAccount(request):
    brand_data = brand.objects.all()
    category_data = item_category.objects.all()
    main_category_data = main_category.objects.all()
    if 'user_id'in request.session:
        if request.session['user_id']!=None:
            user_id = request.session['user_id']
            user_data = Users.objects.filter(user_id=user_id)
            user_addresses = address.objects.filter(user_fk=user_id)
            context = {
                'user_data': user_data[0],
                'user_addresses': user_addresses,
                'brand_data':brand_data,
                'category_data':category_data,
                'main_category_data':main_category_data,
            }
            return render(request, 'myAccount.html',context)
        else:
            return redirect(LoginRegister)
    else:
            return redirect(LoginRegister)
    
def AddAddress(request):
    return render(request,'addressadd.html')

def address_form_view(request):
    if request.method == 'POST':
        # Get the user ID from the session
        user_id = request.session.get("user_id")
        # Retrieve the user instance from the database
        user_instance = Users.objects.get(user_id=user_id)
        house_no = request.POST.get('house_no')
        residence_name = request.POST.get('residence_name')
        landmark = request.POST.get('landmark')
        city = request.POST.get('city')
        pin_code = request.POST.get('pin_code')
        state = request.POST.get('state')
        country = request.POST.get('country')
        deliver_to_whom = request.POST.get('deliver_to_whom')
        deliver_to_contact = request.POST.get('deliver_to_contact')
        # Create a new address instance with the retrieved values
        new_address = address.objects.create(
            address_id=str(uuid.uuid4()),  # Generate a unique address ID
            house_no=house_no,
            user_fk=user_instance,
            residence_name=residence_name,
            landmark=landmark,
            city=city,
            pin_code=pin_code,
            state=state,
            country=country,
            deliver_to_whom=deliver_to_whom,
            deliver_to_contact=deliver_to_contact,
        )
        # Save the new address instance
        new_address.save()
        # Get all addresses for the user
        user_addresses = address.objects.filter(user_fk=user_instance)
        # Display a success message
        success_message = 'Address saved successfully!'
        # Render the checkout page with the success message and user addresses
        return redirect('myAccountPage')
    return render(request, 'addressadd.html')

def address_edit(request,address_id):
    request.session['address_id'] = address_id
    context = {
        'address_id':address_id,
        }
    return render(request,'addressedit.html',context)

def EditAddress(request):
    if request.method == 'POST':
        user_id = request.session.get("user_id")
        user_instance = Users.objects.get(user_id=user_id)
        address_id = request.session['address_id']
        address_instance = get_object_or_404(address, address_id=address_id)
        del request.session['address_id']
        new_house_no = request.POST.get('house_no')
        if new_house_no:
            address.objects.filter(address_id=address_id).update(house_no=new_house_no)
        new_residence_name = request.POST.get('residence_name')
        if new_residence_name:
            address.objects.filter(address_id=address_id).update(residence_name=new_residence_name)
        new_landmark = request.POST.get('landmark')
        if new_landmark:
            address.objects.filter(address_id=address_id).update(landmark=new_landmark)
        new_city = request.POST.get('city')
        if new_city:
            address.objects.filter(address_id=address_id).update(city=new_city)
        new_pin_code = request.POST.get('pin_code')
        if new_pin_code:
            address.objects.filter(address_id=address_id).update(pin_code=new_pin_code)
        new_state = request.POST.get('state')
        if new_state:
            address.objects.filter(address_id=address_id).update(state=new_state)
        new_country = request.POST.get('country')
        if new_country:
            address.objects.filter(address_id=address_id).update(country=new_country)
        new_deliver_to_whom = request.POST.get('deliver_to_whom')
        if new_deliver_to_whom:
            address.objects.filter(address_id=address_id).update(deliver_to_whom=new_deliver_to_whom)
        new_deliver_to_contact = request.POST.get('deliver_to_contact')
        if new_deliver_to_contact:
            address.objects.filter(address_id=address_id).update(deliver_to_contact=new_deliver_to_contact)
        return redirect('myAccountPage')