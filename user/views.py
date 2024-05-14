from django.http import Http404
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.urls import reverse
from user.models import *
from panel.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.

def index(request):
    queryset=slide.objects.all()
    queryset1=about.objects.first()
    printing_items = main.objects.all()
    combined_queryset =  list(printing_items)  
    reviews=review.objects.all() 
    blogs1=blog.objects.all()
    category1=category.objects.all()
    deal1=deal.objects.all()
    context={'slide':queryset,
             'about':queryset1,
             'combined':combined_queryset,
             'reviews':reviews,
             'blogs1':blogs1,
             'category1':category1,
             'deal1':deal1,
             }
    return render(request,'index.html',context)

def gifting1(request):
    default_sort = 'menu_order'
    
    # Retrieve the selected sorting option from the request
    sort_option = request.GET.get('sort', default_sort)
    
    # Retrieve the selected price range from the request
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    
    # Determine the sorting criteria based on the selected option
    if sort_option == 'price':
        # Sort by price: low to high
        gifting = main.objects.all().order_by('-price')
    elif sort_option == 'price-desc':
        # Sort by price: high to low
        gifting = main.objects.all().order_by('price')
    else:
        # Default sorting
        gifting = main.objects.all()
    
    # Apply price range filter if min_price and max_price are provided
    if min_price is not None and max_price is not None:
        gifting = gifting.filter(price__gte=min_price, price__lte=max_price)

    # Retrieve all categories
    categories = category.objects.all()
    
    # Prepare context data to pass to the template
    context = {
        'gifting': gifting,
        'sort_direction': sort_option,
        'category': categories
    }
    
    # Render the template with the context data
    return render(request, 'gifting.html', context)

def printing(request):
    default_sort = 'menu_order'
    
    # Retrieve the selected sorting option from the request
    sort_option = request.GET.get('sort', default_sort)
    
    # Retrieve the selected price range from the request
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    
    # Determine the sorting criteria based on the selected option
    if sort_option == 'price':
        # Sort by price: low to high
        gifting = main.objects.all().order_by('price')
    elif sort_option == 'price-desc':
        # Sort by price: high to low
        gifting = main.objects.all().order_by('-price')
    else:
        # Default sorting
        gifting = main.objects.all()
    
    # Apply price range filter if min_price and max_price are provided
    if min_price is not None and max_price is not None:
        gifting = gifting.filter(price__gte=min_price, price__lte=max_price)

    # Retrieve all categories
    categories = category.objects.all()
    
    # Prepare context data to pass to the template
    context = {
        'printing': gifting,
        'sort_direction': sort_option,
        'category': categories
    }
    
    # Render the template with the context data
    return render(request,'printing.html',context)

def blogs(request):
    queryset=blog.objects.all()
    context={'blog':queryset}
    return render(request,'blogs.html',context)

def blog_details(request,id):
    print(id)
    queryset=blog.objects.get(id=id)
    context={'main':queryset}
    return render(request,'blog-details.html',context)

def product_details(request):
    return render(request,'product-details.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def contact1(request):
    if request.method == 'POST':
            data=request.POST
            name=data.get('name')
            email=data.get('email')
            Number=data.get('number')
            category=data.get('category')
            message=data.get('message')
            print(name,email,Number,category,message)
            message = f"Hello Wrap N Print, someone has sent a message to you with following details:\nName:{name}\nEmail:{email}\ncontact:{Number}\nmessage:{message}"
            send_mail("Wrap N Print!", message, settings.EMAIL_HOST_USER, ['devdave986@gmail.com','sharmabhumi2000@gmail.com'])
            contact.objects.create(
                name=name,
                email=email,
                Number=Number,
                category=category,
                message=message
            )
    return render(request,'contact.html')


def method(request):
    return render(request,'admin1/index.html')


def productdetails1(request,id):
    print(id)
    queryset=main.objects.get(id=id)
    context={'main':queryset}
    return render(request,'product-details.html',context)

def register(request):
    if request.method=='POST':
         data=request.POST
         email=data.get('email')
         password=data.get('password')
         user=User.objects.filter(username=email)
         if user.exists():
              return redirect('/user/register')
         
         user=User.objects.create(username=email,password=password)
         user.set_password(password)
         user.save()
         return redirect('/user/register')
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        data = request.POST
        email = data.get('email')
        password = data.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            request.session['email'] = email
            return redirect('../index/')  # Replace 'home' with the appropriate URL name
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    return render(request, 'login.html')
        
def logout(request):
    del request.session['email']
    return render(request, 'login.html')

from django.http import HttpResponseRedirect

def cart1(request, id=None, email=None):
    if id is not None and email is not None:  # Check both id and email
        try:
            # Check if the product with the given id already exists in the cart
            if cart.objects.filter(productid=id, productemail=email).exists():
               return redirect('/user/cart1/')

            # If the product doesn't exist in the cart, proceed to add it
            queryset = main.objects.get(id=id)
            productid = queryset.id
            productname = queryset.name
            productimage = queryset.img
            productprice = queryset.price

            cart.objects.create(
                productid=productid,
                productname=productname,
                productimage=productimage,
                productprice=productprice,
                productemail=email
            )
        except main.DoesNotExist:
            raise Http404("Product does not exist")

        # Redirect to the same view without parameters to remove them from the URL
        return HttpResponseRedirect('/user/cart1/')
    elif id is not None and email is None:
        return redirect('/user/login/')
    else:
        if request.method == 'POST':
            all_products = request.POST.getlist('product_name')
            all_prices = request.POST.getlist('product_price')
            all_quantities = request.POST.getlist('quantity')
            all_subtotals = request.POST.getlist('subtotal')
            email = request.POST.get('email')

            for product_name, product_price, quantity, subtotal in zip(all_products, all_prices, all_quantities, all_subtotals):
                CartItem.objects.create(
                    product_name=product_name,
                    product_price=product_price,
                    quantity=quantity,
                    subtotal=subtotal,
                    email=email
                )
            checkout_url = reverse('checkout', kwargs={'email': email})
            return HttpResponseRedirect(checkout_url)
        
        all_products = cart.objects.all()
        return render(request, 'cart.html', {'all_products': all_products})

def deleterow10(request,id):
    print(id)
    queryset=cart.objects.get(id=id)
    queryset.delete()
    return redirect('/user/cart1/')

from django.shortcuts import render

def checkout1(request,email):
    if email is not None:  
        if CartItem.objects.filter(email=email).exists():
            all_products = CartItem.objects.all()

        if cart.objects.filter(productemail=email).exists():
            all_products_1 = cart.objects.all()

        if request.method == 'POST':
                data=request.POST
                name=data.get('name')
                email=data.get('email')
                number=data.get('number')
                upi_id=data.get('upi_id')
                address=data.get('address')
                img=request.FILES.get('img')
                total=data.get('total')
                cart_items = CartItem.objects.all()  
                context = {'name': name, 'email': email, 'number': number,'total':total,'cart_items': cart_items }
                html_message = render_to_string('email.html', context)
                plain_message = strip_tags(html_message)  # Strip HTML tags for the plain text version
                subject = 'Message from Website'
                send_mail(subject, plain_message, settings.EMAIL_HOST_USER, [email], html_message=html_message)

                checkout.objects.create(
                    name=name,
                    email=email,
                    number=number,
                    upi_id=upi_id,
                    address=address,
                    img=img,
                    total=total
                
                )
                for cart_item in all_products:
                    OrderItem.objects.create(
                    product_name=cart_item.product_name,
                    product_price=cart_item.product_price,
                    quantity=cart_item.quantity,
                    subtotal=cart_item.subtotal,
                    email=cart_item.email
                    )
                all_products.delete()
                all_products_1.delete()
                return HttpResponseRedirect('/user/thankyou')
        context={'main':all_products}
    return render(request, 'checkout.html',context)


def deleterow11(request,id):
    print(id)
    queryset=CartItem.objects.get(id=id)
    queryset.delete()
    return redirect('/user/checkout/dev@gmail.com/')

def thankyou(request):
    return render(request,'thankyou.html')


def wishlist1(request, id=None, email=None):
    if id is not None and email is not None:  # Check both id and email
        try:
            # Check if the product with the given id already exists in the cart
            if wishlist.objects.filter(productid=id, productemail=email).exists():
                return redirect('/user/wishlist/')
            
            # If the product doesn't exist in the cart, proceed to add it
            queryset = main.objects.get(id=id)
            productid = queryset.id
            productname = queryset.name
            productimage = queryset.img
            productprice = queryset.price

            wishlist.objects.create(
                productid=productid,
                productname=productname,
                productimage=productimage,
                productprice=productprice,
                productemail=email
            )
            
            # Redirect to wishlist page immediately after adding the item
            return redirect('/user/wishlist/')
            
        except main.DoesNotExist:
            raise Http404("Product does not exist")
        
    elif id is not None and email is None:
        return redirect('/user/login/')
    else:
        all_products = wishlist.objects.all()
        return render(request, 'wishlist.html', {'all_products': all_products})


def deleterow14(request,id):
    print(id)
    queryset=wishlist.objects.get(id=id)
    queryset.delete()
    return redirect('/user/wishlist')