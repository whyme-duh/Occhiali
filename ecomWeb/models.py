from django.db import models
from PIL import Image
from django.contrib.auth.models import User
import datetime
from phone_field import PhoneField




class Category(models.Model):
    name = models.CharField(max_length=80, default='', blank = False)

    def __str__(self):
        return self.name

class Product(models.Model):
    standard = "Standard(54-18)"
    extrasmall = "Extra Small(52-16)"
    small = "Small(54-16)"

    size_choices = [
        (standard ,"Standard(54-18)"),
        (extrasmall , "Extra Small(52-16)"),
        (small,"Small(54-16)"),
    ]

    eyeglasses = "eyeglasses"
    sunglasses = "sunglasses"

    glasses_type_choices = [
        (eyeglasses , "Eyeglasses"),
        (sunglasses , "Sunglasses"),
    ]

    name = models.CharField(max_length=150)
    first_long_product = models.BooleanField(null = True, blank = True, default= False)
    last_long_product = models.BooleanField(null = True, blank = True, default= False)
    glasses_type = models.CharField(max_length=80, default="Eyeglasses", choices=glasses_type_choices)
    discount_price = models.IntegerField(blank=True, null=True)
    include_offer = models.BooleanField(default=False)
    people_img = models.URLField(null=True, blank=False)
    upper_img = models.URLField(null=True, blank=False)
    lower_image = models.URLField(null=True, blank=False)
    brand = models.CharField(max_length=80, null=True)
    price = models.IntegerField()
    color = models.Choices
    frame_color = models.CharField(max_length=100, null=True)
    frame_material = models.CharField(max_length=100, null=True)
    frame_treatment = models.CharField(max_length=100, null=True)
    frame_shape = models.CharField(max_length=100, null=True)
    lens_color = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    size = models.CharField(max_length = 100 , choices=size_choices, default="Standard(54-16)")
    slug = models.SlugField()
    

    

    def __str__(self):
        return self.name
    



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
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = True )
    fname = models.CharField(max_length=80, null = False)
    lname = models.CharField(max_length=80, null = False)
    address = models.CharField(max_length=100, null= False)
    phone = PhoneField(blank=False)
    total_price =models.FloatField(null = False)
    payment_id = models.CharField(max_length = 250, null = True)
    order_status = (
        ("Pending ", "Pending"),
        ("Out for Shipping" , "Out for Shipping"),
        ("Delivered", "Delivered")
    )
    status = models.CharField(max_length=100, choices=order_status, default="Pending", null= False)
    message = models.TextField(null = True)
    tracking_no = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    payment_completed = models.BooleanField(default=False) 


    def __str__(self):
        return ' {} -{}'.format(self.id, self.tracking_no)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(null = False)
    
    def __str__(self):
        return f'{self.order}'
    



    


    


