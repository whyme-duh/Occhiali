from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from ecomWeb.models import Product, CartItems, Cart
import datetime 

# Create your models here.

class Profile(models.Model):
    image = models.ImageField(upload_to='profile', default='default.jpg')
    phone = PhoneField(blank= True, null=True)
    user = models.OneToOneField(User, on_delete= models.CASCADE, default=True)
    
    def __str__(self):
        return self.user.username
    
    def get_cart_count (self):
        return CartItems.objects.filter(cart__is_paid = False, cart__user = self.user).count()
    
    





class BillingAdress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default = True )
    first_name = models.CharField(max_length=80, null = False)
    last_name = models.CharField(max_length=80, null = False)
    address1 = models.CharField(max_length=100, null= False)
    phone = PhoneField(blank=False)


    def __str__(self):
        return self.first_name
    

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default = True )
    product = models.OneToOneField(Product, on_delete=models.CASCADE, default=True)

    def __str__(self):
        return self.product.name
