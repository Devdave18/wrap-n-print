"""
URL configuration for wrap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views import *
# from admin1.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('index/',index),
    path('gifting/',gifting1),
    path('printing/',printing),
    path('blogs/',blogs),
    path('blog_details/<int:id>/',blog_details),
    path('product_details/',product_details),
    path('cart/',cart),
    path('login/',login),
    path('register/',register),
    path('contact/',contact1),
    path('productdetails1/<id>/',productdetails1),
    path('register/',register),
    path('login/',login),
    path('logout/',logout),
    path('cart1/', cart1),
    path('cart1/<int:id>/', cart1),
    path('cart1/<int:id>/<str:email>/', cart1),
    path('deleterow10/<id>/',deleterow10),
    path('deleterow11/<id>/',deleterow11),
    path('checkout/<str:email>/',checkout1,name='checkout'),
    path('thankyou',thankyou),
    path('wishlist/', wishlist1),
    path('wishlist/<int:id>/<str:email>/', wishlist1),
    path('wishlist/<int:id>/', wishlist1),
    path('deleterow14/<id>/',deleterow14),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
