from django.shortcuts import render
from django.shortcuts import render,redirect
from django.urls import reverse
from panel.models import *
from user.models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib.auth.hashers import check_password

# .Create your views here.
def main1(request):
    if request.method == 'POST':
            data=request.POST
            name=data.get('name')
            price=data.get('price')
            description=data.get('description')
            img=request.FILES.get('img')
            sale=data.get('sale')
            sku=data.get('sku')
            category=data.get('category')
            sub_category=data.get('sub_category')
            tags=data.get('tags')
            img2=request.FILES.get('img2')
            img3=request.FILES.get('img3')
            img4=request.FILES.get('img4')
            rate=data.get('rate')
            discount=data.get('discount')
            type=data.get('type')

            print(name,price,description,img,sale,sku,category,sub_category,tags,img2,img3,img4,rate,discount,type)

            main.objects.create(
                name=name,
                price=price,
                description=description,
                img=img,
                sale=sale,
                sku=sku,
                category=category,
                sub_category=sub_category,
                tags=tags,
                img2=img2,
                img3=img3,
                img4=img4,
                rate=rate,
                discount=discount,
                type=type
            )
    queryset=main.objects.all()
    context={'main':queryset}
    return render(request,'print.html',context)

def deleterow(request,id):
    print(id)
    queryset=main.objects.get(id=id)
    queryset.delete()
    return redirect('/panel/main1/')


def main3(request):
    if request.method == 'POST':
            data=request.POST
            title=data.get('title')
            img1=request.FILES.get('img1')
            img2=request.FILES.get('img2')
            img3=request.FILES.get('img3')
            description1=data.get('description1')
            description2=data.get('description2')
            description3=data.get('description3')
            date=data.get('date')
            author=data.get('author')
           
            print(title,img1,img2,img3,description1,description2,description3,date,author)

            blog.objects.create(
                title=title,
                img1=img1,
                img2=img2,
                img3=img3,
                description1=description1,
                description2=description2,
                description3=description3,
                date=date,
                author=author
            )
    queryset=blog.objects.all()
    context={'blog':queryset}
    return render(request,'blogs1.html',context)

def deleterow2(request,id):
      print(id)
      queryset=blog.objects.get(id=id)
      queryset.delete()
      return redirect('/panel/blogg/')

def main4(request):
    if request.method == 'POST':
            data=request.POST
            name=data.get('name')
            email=data.get('email')
            number=data.get('number')
            category=data.get('category')
            message=data.get('message')

            print(name,email,number,category,message)
            
            contact3.objects.create(
                name=name,
                email=email,
                number=number,
                category=category,
                message=message
            )
    queryset=contact3.objects.all()
    context={'contact3':queryset}
    return render(request,'contactus.html',context)

def deleterow3(request,id):
      print(id)
      queryset=contact3.objects.get(id=id)
      queryset.delete()
      return redirect('/panel/contactus/')

def main5(request):
    if request.method == 'POST':
            data=request.POST
            heading=data.get('heading')
            content=data.get('content')
            img1=request.FILES.get('img1')

            print(heading,content,img1)
            
            about.objects.create(
                heading=heading,
                content=content,
                img1=img1,
            )
    queryset=about.objects.all()
    context={'about':queryset}
    return render(request,'about.html',context)

def deleterow4(request,id):
      print(id)
      queryset=about.objects.get(id=id)
      queryset.delete()
      return redirect('/panel/about/')

def main6(request):
    if request.method == 'POST':
            data=request.POST
            heading=data.get('heading')
            title=data.get('title')
            img=request.FILES.get('img')
            phoneimg=request.FILES.get('phoneimg')

            print(heading,title,img,phoneimg)
            
            slide.objects.create(
                heading=heading,
                title=title,
                img=img,
                phoneimg=phoneimg,
            )
    queryset=slide.objects.all()
    context={'slide':queryset}
    return render(request,'slider.html',context)

def deleterow5(request,id):
      print(id)
      queryset=slide.objects.get(id=id)
      queryset.delete()
      return redirect('/panel/slide/')

def main7(request):
    if request.method == 'POST':
            data=request.POST
            reviews=data.get('reviews')
            name=data.get('name')
            designation=data.get('designation')
            img=request.FILES.get('img')

            print(reviews,name,designation,img)
            
            review.objects.create(
                reviews=reviews,
                name=name,
                designation=designation,
                img=img
            )
    queryset=review.objects.all()
    context={'review':queryset}
    return render(request,'testimonials.html',context)

def deleterow6(request,id):
      print(id)
      queryset=review.objects.get(id=id)
      queryset.delete()
      return redirect('/panel/review/')

def main8(request):
    if request.method == 'POST':
            data=request.POST
            img=request.FILES.get('img')
            title=data.get('title')

            print(img,title)
            
            category.objects.create(
                img=img,
                title=title
            )
    queryset=category.objects.all()
    context={'category':queryset}
    return render(request,'category.html',context)

def deleterow7(request,id):
      print(id)
      queryset=category.objects.get(id=id)
      queryset.delete()
      return redirect('/panel/category/')


def main9(request):
    if request.method == 'POST':
            data=request.POST
            img=request.FILES.get('img')
            date=data.get('date')
            link=data.get('link')

            print(img,date,link)
            
            deal.objects.create(
                img=img,
                date=date,
                link=link
            )
    queryset=deal.objects.all()
    context={'deal':queryset}
    return render(request,'deal.html',context)

def deleterow8(request,id):
      print(id)
      queryset=deal.objects.get(id=id)
      queryset.delete()
      return redirect('/panel/deal/')


def aboutup(request,id):
    print(id)
    queryset=about.objects.get(id=id)
    if request.method == 'POST':
        data=request.POST
        heading=data.get('heading')
        content=data.get('content')
        img1=request.FILES.get('img1')
        if img1:
            queryset.img1 = img1
        queryset.heading=heading
        queryset.content=content
        queryset.save()
        return redirect('../../about/')
    context={'about':queryset}
    
    return render(request,'update_about.html',context)


def blogup(request,id):
    print(id)
    queryset=blog.objects.get(id=id)
    if request.method == 'POST':
        data=request.POST
        title=data.get('title')
        img1=request.FILES.get('img1')
        img2=request.FILES.get('img2')
        img3=request.FILES.get('img3')
        description1=data.get('description1')
        description2=data.get('description2')
        description3=data.get('description3')
        date=data.get('date')
        author=data.get('author')
        if img1:
            queryset.img1 = img1
        if img2:
            queryset.img2 = img2
        if img3:
            queryset.img3 = img3
        queryset.title=title
        queryset.description1=description1
        queryset.description2=description2
        queryset.description3=description3
        queryset.date=date
        queryset.author=author           
        queryset.save()
        return redirect('../../blogg/')
    context={'blog':queryset}
    
    return render(request,'update_blogs1.html',context)


def categoryup(request,id):
    print(id)
    queryset=category.objects.get(id=id)
    if request.method == 'POST':
        data=request.POST
        img=request.FILES.get('img')
        title=data.get('title')

        if img:
            queryset.img = img
        queryset.title=title     
        queryset.save()
        return redirect('../../category/')
    context={'category':queryset}
    
    return render(request,'update_category.html',context)


def dealup(request,id):
    print(id)
    queryset=deal.objects.get(id=id)
    if request.method == 'POST':
        data=request.POST
        img=request.FILES.get('img')
        date=data.get('date')
        link=data.get('link')
        if img:
            queryset.img = img
        queryset.date=date
        queryset.link=link
        queryset.save()
        return redirect('../../deal/')
    context={'deal':queryset}
    
    return render(request,'update_deal.html',context)

from django.contrib.auth.hashers import make_password

def contactup(request,id):
    print(id)
    queryset= User.objects.get(id=id)

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Update the user's email
        queryset.email = email
        
        # Set the user's password
        queryset.password = make_password(password)
        
        queryset.save()
        return redirect('../../user/') 
    
    context = {'user': queryset}
    return render(request, 'update_user.html', context)



def printup(request, id):
    print(id)
    queryset = main.objects.get(id=id)
    
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        price = data.get('price')
        description = data.get('description')
        img = request.FILES.get('img')
        sale = data.get('sale')
        sku = data.get('sku')
        category = data.get('category')
        sub_category = data.get('sub_category')
        tags = data.get('tags')
        img2 = request.FILES.get('img2')
        img3 = request.FILES.get('img3')
        img4 = request.FILES.get('img4')
        rate = data.get('rate')
        discount = data.get('discount')
        type = data.get('type')
        
        # Check if image fields are empty
        if img:
            queryset.img = img

        if img2:
             queryset.img2 = img2
        if img3:
             queryset.img3 = img3
        if img4:
             queryset.img4 = img4
        
        queryset.name = name
        queryset.price = price
        queryset.description = description
        queryset.sale = sale
        queryset.sku = sku
        queryset.category = category
        queryset.sub_category = sub_category
        queryset.tags = tags
        queryset.rate = rate
        queryset.discount = discount
        queryset.type = type
        queryset.save()
        return redirect('../../main1/')
    
    context = {'main': queryset}
    return render(request, 'update_print.html', context)

def slideup(request, id):
    print(id)
    queryset = slide.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        heading = data.get('heading')
        title = data.get('title')
        new_img = request.FILES.get('img')
        phoneimg=request.FILES.get('phoneimg')

        # Check if a new image is selected
        if new_img:
            queryset.img = new_img
        if phoneimg:
             queryset.phoneimg = phoneimg

        queryset.heading = heading
        queryset.title = title
        queryset.save()
        return redirect('../../slide/')
    context = {'slide': queryset}
    
    return render(request, 'update_slider.html', context)

def testimonials(request,id):
    print(id)
    queryset=review.objects.get(id=id)
    if request.method == 'POST':
        data=request.POST
        reviews=data.get('reviews')
        name=data.get('name')
        designation=data.get('designation')
        img=request.FILES.get('img')
        if img:
            queryset.img = img

        queryset.reviews=reviews
        queryset.name=name
        queryset.designation=designation
         
        queryset.save()
        return redirect('../../review/')
    context={'review':queryset}
    
    return render(request,'update_testimonials.html',context)

def user(request):
    queryset=User.objects.all()
    context={'user':queryset}
    return render(request,'user.html',context)


def deleterow9(request,id):
      print(id)
      queryset=User.objects.get(id=id)
      queryset.delete()
      return redirect('/panel/user/')

from django.contrib.auth.hashers import check_password

def login1(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        
        admin_users = adminpanel.objects.filter(email=email)
        
        if admin_users.exists():
            for admin_user in admin_users:
                if password == admin_user.password:
                    request.session['email'] = email
                    return redirect(reverse('slide'))  # Assuming 'slide' is the URL name for your slide view
            
            # If password doesn't match for any user
            error_message = 'Invalid password. Please try again.'
        else:
            # If no user found with the given email
            error_message = 'No user found with the given email.'

        return render(request, 'login1.html', {'error_message': error_message})
    
    return render(request, 'login1.html')



def logout(request):
    del request.session['email']
    return redirect('/panel/login1/')


def checkout2(request):
    queryset=checkout.objects.all()
    context={'checkout':queryset}
    return render(request,'payment.html',context)
   

def deleterow10(request,id):
      print(id)
      queryset=checkout.objects.get(id=id)
      queryset.delete()
      return redirect('/panel/checkout2/')

def checkout1(request):
    queryset=checkout.objects.all()
    context={'checkout':queryset}
    return render(request,'checkout1.html',context)

def deleterow12(request,id):
      print(id)
      queryset=checkout.objects.get(id=id)
      queryset.delete()
      return redirect('/panel/checkout1/')



def Orderitem1(request):
    queryset=OrderItem.objects.all()
    context={'OrderItem':queryset}
    return render(request,'Orderitem.html',context)


def deleterow13(request,id):
      print(id)
      queryset=OrderItem.objects.get(id=id)
      queryset.delete()
      return redirect('/panel/Orderitem1/')
