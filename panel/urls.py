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
from panel.views import *
# from admin1.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('main1/',main1),
    path('deleterow/<id>/',deleterow),
    path('blogg/',main3),
    path('deleterow2/<id>/',deleterow2),
    path('contactus/',main4),
    path('deleterow3/<id>/',deleterow3),
    path('about/',main5),
    path('deleterow4/<id>/',deleterow4),
    path('slide/',main6, name='slide'),
    path('deleterow5/<id>/',deleterow5),
    path('review/',main7),
    path('deleterow6/<id>/',deleterow6),
    path('category/',main8),
    path('deleterow7/<id>/',deleterow7),
    path('deal/',main9),
    path('deleterow8/<id>/',deleterow8),
    path('aboutup/<id>/',aboutup),
    path('blogup/<id>/',blogup),
    path('categoryup/<id>/',categoryup),
    path('contactup/<id>/',contactup),
    path('dealup/<id>/',dealup),
    path('printup/<id>/',printup),
    path('slideup/<id>/',slideup),
    path('testimonials/<id>/',testimonials),
    path('user/',user),
    path('deleterow9/<id>/',deleterow9),
    path('login1/',login1,name='login1'),
    path('logout/',logout),
    path('checkout2/',checkout2),
    path('deleterow10/<id>/',deleterow10),
    path('checkout1/',checkout1),
    path('Orderitem1/',Orderitem1),
    path('deleterow12/<id>/',deleterow12),
    path('deleterow13/<id>/',deleterow13),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


