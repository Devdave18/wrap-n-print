from django.db import models
from django.shortcuts import render,redirect
from panel.models import *
from django.contrib.auth.hashers import make_password


# Create your models here.

class main(models.Model):
    name=models.CharField(max_length=20)
    price=models.CharField(max_length=20)
    description=models.CharField(max_length=20)
    img=models.ImageField(upload_to="images/",blank=True,null=True)
    sale=models.CharField(max_length=20)
    sku=models.CharField(max_length=20)
    category=models.CharField(max_length=20,blank=True,null=True)
    sub_category=models.CharField(max_length=20,blank=True,null=True)
    tags=models.CharField(max_length=20)
    img2=models.ImageField(upload_to="images/",blank=True,null=True)
    img3=models.ImageField(upload_to="images/",blank=True,null=True)
    img4=models.ImageField(upload_to="images/",blank=True,null=True)
    rate=models.CharField(max_length=20)
    discount=models.CharField(max_length=20)
    type=models.CharField(max_length=20,blank=True,null=True)



def __str__(self):
    return f"{self.name,self.price,self.description,self.img,self.sale,self.sku,self.category,self.sub_category,self.tags,self.img2,self.img3,self.img4,self.rate,self.discount}"

class blog(models.Model):
    title=models.CharField(max_length=20)
    img1=models.ImageField(upload_to="images/",blank=True,null=True)
    img2=models.ImageField(upload_to="images/",blank=True,null=True)
    img3=models.ImageField(upload_to="images/",blank=True,null=True)
    description1=models.CharField(max_length=20)
    description2=models.CharField(max_length=20)
    description3=models.CharField(max_length=20)
    date=models.DateField()
    author=models.CharField(max_length=20)

def __str__(self):
    return f"{self.title,self.img1,self.img2,self.img3,self.description1,self.description2,self.description3,self.date,self.author}"

class contact3(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    number=models.CharField(max_length=15,blank=True,null=True)
    category=models.CharField(max_length=20)
    message=models.CharField(max_length=20)

def __str__(self):
    return f"{self.name,self.email,self.Number,self.category,self.message}"

class about(models.Model):
    heading=models.CharField(max_length=20)
    content=models.CharField(max_length=20)
    img1=models.ImageField(upload_to="images/",blank=True,null=True)

def __str__(self):
    return f"{self.heading,self.content,self.img1,self.img2,self.link1,self.link2}"

class slide(models.Model):
    heading=models.CharField(max_length=20)
    title=models.CharField(max_length=20)
    img=models.ImageField(upload_to="images/",blank=True,null=True)
    phoneimg=models.ImageField(upload_to="image/",blank=True,null=True)

def __str__(self):
    return f"{self.heading,self.title,self.img}"

class review(models.Model):
    reviews=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    designation=models.CharField(max_length=20)
    img=models.ImageField(upload_to="images/",blank=True,null=True)

def __str__(self):
    return f"{self.reviews,self.name,self.designation,self.img}"

class category(models.Model):
    img=models.ImageField(upload_to="images/",blank=True,null=True)
    title=models.CharField(max_length=20)
    

def __str__(self):
    return f"{self.img,self.title}"

class deal(models.Model):
     img=models.ImageField(upload_to="images/",blank=True,null=True)
     date=models.DateField()
     link=models.CharField(max_length=20)

def __str__(self):
    return f"{self.img,self.date,self.link}"

class adminpanel(models.Model):
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=128)  # Store hashed password
    
    def save(self, *args, **kwargs):
        # Hash the password before saving
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

