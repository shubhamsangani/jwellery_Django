from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from adminpanel.models import *
import random
import uuid
import string
from products.models import *
from django.core.files.storage import FileSystemStorage


def custom_authenticate(admin_username, admin_password):
    try:
        admin_user = AdminUsers.objects.get(admin_user_name=admin_username)
        if admin_user.admin_user_password == admin_password:
            return admin_user
    except AdminUsers.DoesNotExist:
        return None

def AdminLoginRegister(request):
    form_data = {
        'admin_user_name': '',
        'admin_user_email': '',
        'admin_user_phone_number': '',
        'admin_user_password': '',
        'admin_repeat_password': '',
    }

    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        print("Form type:", form_type)  # Debugging
        
        if form_type == 'login':
            admin_username = request.POST.get('admin_login_username')
            admin_password = request.POST.get('admin_login_password')

            # Check if username and password are provided
            if admin_username and admin_password:
                admin_user = custom_authenticate(admin_username, admin_password)
                if admin_user is not None:
                    # Set session or cookie to indicate user is logged in
                    request.session['admin_user_id'] = admin_user.admin_user_id
                    print("User logged in:", admin_user.admin_user_name)
                    return redirect('adminmyaccountPage')  # Redirect to home page after successful login
                else:
                    messages.error(request, "Invalid username or password.")
                    print("Authentication failed for user:", admin_username)
            else:
                messages.error(request, "Username and password are required.")
                print("Authentication failed: Username or password not provided.")

        elif form_type == 'signup':
            form_data['admin_user_name'] = request.POST.get('admin_user_name').strip()
            form_data['admin_user_email'] = request.POST.get('admin_user_email').strip()
            form_data['admin_user_phone_number'] = request.POST.get('admin_user_phone_number').strip()
            form_data['admin_user_password'] = request.POST.get('admin_user_password').strip()
            form_data['admin_repeat_password'] = request.POST.get('admin_repeat_password').strip()

            if any(value == '' for value in form_data.values()):
                messages.error(request, "All fields are required!!")
            else:
                if form_data['admin_user_password'] != form_data['admin_repeat_password']:
                    messages.error(request, "Passwords do not match!!")
                else:
                    randomstr = ''.join(random.choices(string.ascii_lowercase + string.digits, k=15))
                    uniqueID = "BroaderAI_user_information_" + randomstr
                    active = "On"

                    admin_user = AdminUsers(
                        admin_user_id=uniqueID,
                        admin_user_name=form_data['admin_user_name'],
                        admin_user_email=form_data['admin_user_email'],
                        admin_user_phone_no=form_data['admin_user_phone_number'],
                        admin_user_password=form_data['admin_user_password'],
                        admin_user_is_active=active,
                    )
                    admin_user.save()

                    if admin_user.admin_user_id:
                        messages.success(request, "User added successfully!!")
                        print("User added successfully:", admin_user.admin_user_name)  # Debugging
                        return redirect('adminloginregisterPage')  # Redirect to the correct URL after successful signup
                    else:
                        messages.error(request, "Something went wrong!!")
                        print("Error: Something went wrong while saving user.")  # Debugging

    return render(request, "adminloginRegister.html", {'form_data': form_data})

def adminmyaccount(request):
    admin_user_info = None
    admin_user_id = request.session.get('admin_user_id')

    if admin_user_id:
        admin_user_info = AdminUsers.objects.filter(admin_user_id=admin_user_id).first()
    return render(request, "adminmyaccount.html", {'admin_user_info': admin_user_info})

def product_details(request):
    admin_user_info = None
    admin_user_id = request.session.get('admin_user_id')
    if admin_user_id:
        admin_user_info = AdminUsers.objects.filter(admin_user_id=admin_user_id).first()
    
    all_products = product.objects.all()

    product_brand_dict = {}
    # Fetch product brands and store them in the dictionary
    for i in product_brand.objects.select_related('brand_fk').filter(product_fk__in=all_products):
        if i.brand_fk.brand_name == admin_user_info.admin_user_name:
            product_brand_dict[i.product_fk_id] = admin_user_info.admin_user_name
    
    product_ids = list(product_brand_dict.keys())
    filtered_products = product.objects.filter(product_id__in=product_ids)

    # Add brand name to each product object using the dictionary
    for product_obj in filtered_products:
        product_obj.brand_name = product_brand_dict.get(product_obj.product_id)

    # Add colors and sizes to each product object
    for i in filtered_products:
        # productt.brand = product_brand.objects.filter(product_fk=productt)
        i.colors = product_color.objects.filter(product_fk=i)
        i.sizes = product_size.objects.filter(product_fk=i)

    return render(request, 'viewproducts.html', {'products': filtered_products})
def addproduct(request):
    admin_user_info = None
    admin_user_id = request.session.get('admin_user_id')
    if admin_user_id:
        admin_user_info = AdminUsers.objects.filter(admin_user_id=admin_user_id).first()

    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'addproduct':
            product_name = request.POST.get('product_name')
            product_description = request.POST.get('product_description')
            product_stock = request.POST.get('product_stock')
            product_prices = request.POST.get('product_price')
            product_discount = request.POST.get('product_discount')
            product_size_values = request.POST.get('product_size').split()  # Split sizes by space
            product_colors = request.POST.getlist('colors[]')
            product_item_category_name= request.POST.get('item')
            selected_category = request.POST.get('gender')


            product_id = str(uuid.uuid4())
            admin_user_id = request.session['admin_user_id']
            try:
                # Check if the brand exists in the database
                brand_obj = brand.objects.get(brand_name=admin_user_info.admin_user_name)
            except brand.DoesNotExist:
                # If the brand does not exist, create a new entry
                brand_id = str(uuid.uuid4())
                brand_obj = brand.objects.create(brand_id=brand_id, brand_name=admin_user_info.admin_user_name, brand_created_at=timezone.now())

            try:
                # Check if the item category exists in the database
                item_obj = item_category.objects.get(item_category_name=product_item_category_name)
            except item_category.DoesNotExist:
                # If the item category does not exist, create a new entry
                item_category_id=str(uuid.uuid4())
                item_obj = item_category.objects.create(item_category_id=item_category_id, item_category_name=product_item_category_name, item_category_created_at=timezone.now())

            
            main_obj = main_category.objects.get(main_category_name=selected_category)
            
            # Create Product instance
            new_product = product(
                product_id=product_id,
                product_name=product_name,
                product_description=product_description,
                product_stock=product_stock,
                product_price=product_prices,
                product_discount=product_discount,
            )
            new_product.save()

            #Saving main category
            product_main.objects.create(product_main_id=str(uuid.uuid4()), product_fk=new_product, main_fk=main_obj)  
            product_brand.objects.create(product_brand_id=str(uuid.uuid4()), product_fk=new_product, brand_fk=brand_obj)
            product_item.objects.create(product_item_id=str(uuid.uuid4()), product_fk=new_product, item_fk=item_obj)

            main_brand_obj = main_brand.objects.create(main_brand_id=str(uuid.uuid4()), main_fk=main_obj, brand_fk=brand_obj)  
            main_item_obj = main_item.objects.create(main_item_id=str(uuid.uuid4()), main_fk=main_obj, item_fk=item_obj)            
            brand_item_obj = brand_item.objects.create(brand_item_id=str(uuid.uuid4()), brand_fk=brand_obj, item_fk=item_obj) 

            product_main_brand.objects.create(product_main_brand_id=str(uuid.uuid4()), product_fk=new_product, main_brand_fk=main_brand_obj)
            product_main_item.objects.create(product_main_item_id=str(uuid.uuid4()), product_fk=new_product, main_item_fk=main_item_obj)
            product_brand_item.objects.create(product_brand_item_id=str(uuid.uuid4()), product_fk=new_product, brand_item_fk=brand_item_obj)

            # Save product image
            product_images = request.FILES.getlist('product_image')
            if product_images:
                for image in product_images:
                    product_image_id = str(uuid.uuid4())
                    # Create a FileSystemStorage instance
                    fs = FileSystemStorage(location=settings.MEDIA_ROOT)

                    # Save the image file with a unique filename
                    filename = fs.save(str(product_image_id) + '_' + image.name, image)

                    # Construct the full image URL using MEDIA_URL
                    image_full_url = settings.MEDIA_URL + filename

                    # Create ProductImage instance and associate it with the product
                    product_image.objects.create(
                        product_fk=new_product, 
                        image_path=image_full_url[:100],  # Save the full image URL
                        product_image_created_at=timezone.now(),
                        product_image_id=product_image_id
                    )

            # Create Product Color instances
            for color_name in product_colors:
                product_color_id=str(uuid.uuid4())
                color_stock = request.POST.get(f'color_stock_{color_name}')
                new_color = product_color(color_name=color_name, product_fk=new_product, color_stock=color_stock, product_color_created_at=timezone.now(), product_color_id=product_color_id)
                new_color.save()

            # Create Product Size instances
            for size_value in product_size_values:
                product_size_id=str(uuid.uuid4())
                new_size = product_size(size_value=size_value, product_fk=new_product,product_size_created_at=timezone.now(), product_size_id=product_size_id)
                new_size.save()

            # Create Product Size-Color combinations
            for color_name in product_colors:
                color_stock = request.POST.get(f'color_stock_{color_name}')

                # Use filter instead of get
                color_instance = product_color.objects.filter(color_name=color_name, product_fk=new_product).first()

                # If the color doesn't exist, create a new one
                if not color_instance:
                    color_instance = product_color(product_color_id=str(uuid.uuid4()), color_name=color_name,product_color_created_at=timezone.now(), product_fk=new_product)
                    color_instance.save()

                # Update the color_stock
                color_instance.color_stock = color_stock
                color_instance.save()

            product_extra_charges = request.POST.get('product_extra_charges')
            product_instance = product.objects.get(product_id=new_product.product_id)
            if product_instance:
                if product_instance.product_discount:
                    discounted_price = product_instance.product_discounted_price
                else:
                    discounted_price=0

            final_charges = float(product_extra_charges) + float(discounted_price)
            product_price.objects.create(product_price_id=str(uuid.uuid4()), product_price=product_prices, extra_charges=product_extra_charges, final_charges=final_charges, product_fk=new_product, size_fk=new_size, color_fk=new_color, product_price_created_at=timezone.now())

            messages.success(request, "Product added successfully!!")
            return redirect('viewproductPage')
    
    return render(request, "addproduct.html", {'admin_user_info': admin_user_info})

def adminlogout(request):
    # Clear the session data
    request.session.clear()
    return redirect('adminloginregisterPage')

def deletepageview(request):
    admin_user_info = None
    admin_user_id = request.session.get('admin_user_id')
    if admin_user_id:
        admin_user_info = AdminUsers.objects.filter(admin_user_id=admin_user_id).first()
    
    # Query products of the session user with their colors and sizes
    all_products = product.objects.all()

    product_brand_dict = {}

    # Fetch product brands and store them in the dictionary
    for product_brand_obj in product_brand.objects.select_related('brand_fk').filter(product_fk__in=all_products):
        if product_brand_obj.brand_fk.brand_name == admin_user_info.admin_user_name:
            product_brand_dict[product_brand_obj.product_fk_id] = admin_user_info.admin_user_name
    product_ids = list(product_brand_dict.keys())

    filtered_products = product.objects.filter(product_id__in=product_ids)

    # Add colors and sizes to each product object
    for i in filtered_products:
        # productt.brand = product_brand.objects.filter(product_fk=productt)
        i.colors = product_color.objects.filter(product_fk=i)
        i.sizes = product_size.objects.filter(product_fk=i)
    return render(request, 'deleteproducts.html', {'products': filtered_products})

def delete_product(request, product_id):
    if request.method == 'POST':
        product_instance = get_object_or_404(product, pk=product_id)
        product_instance.delete()
        return render(request, "viewproducts.html")
