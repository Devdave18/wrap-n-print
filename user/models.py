from django.db import models


# Create your models here.


class contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    Number=models.CharField(max_length=15,blank=True,null=True)
    category=models.CharField(max_length=20)
    message=models.CharField(max_length=20)

def __str__(self):
    return f"{self.name,self.email,self.Number,self.category,self.message}"

class cart(models.Model):
    email=models.CharField(max_length=20)
    productid=models.CharField(max_length=20)
    productname=models.CharField(max_length=20)
    productimage=models.CharField(max_length=20)
    productprice=models.CharField(max_length=20)
    productemail=models.CharField(max_length=20,null=True)

class checkout(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    number=models.CharField(max_length=20)
    upi_id=models.CharField(max_length=30)
    address=models.CharField(max_length=50,null=2)
    img=models.ImageField(upload_to="images/",blank=True,null=True)
    total=models.CharField(max_length=20)

class CartItem(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    email=models.CharField(max_length=20)


class OrderItem(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    email=models.CharField(max_length=20)


class wishlist(models.Model):
    email=models.CharField(max_length=20)
    productid=models.CharField(max_length=20)
    productname=models.CharField(max_length=20)
    productimage=models.CharField(max_length=20)
    productprice=models.CharField(max_length=20)
    productemail=models.CharField(max_length=20,null=True)
