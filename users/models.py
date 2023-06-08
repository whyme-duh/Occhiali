from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from ecomWeb.models import Product
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
    
    


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default = False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null = True)
    order_date = models.DateField(default = datetime.datetime.today)

    def __str__(self):
        return self.is_paid
    
    def get_cart_total(self):
        cart_items = self.cart_items.all()
        price = []
        for cart_item in cart_items:
            price.append(cart_item.product.price)
        return sum(price)
   
    

class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null = True, blank=True)


    def get_price(self):
        price = [self.product.price]
        return sum(price)

class BillingAdress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default = True )
    first_name = models.CharField(max_length=80, null = False)
    last_name = models.CharField(max_length=80, null = False)
    address1 = models.CharField(max_length=100, null= False)
    address2 = models.CharField(max_length=100, null= True, blank = True)
    phone = PhoneField(blank=False)


    def __str__(self):
        return self.first_name