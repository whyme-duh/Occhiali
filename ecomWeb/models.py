from django.db import models
from PIL import Image
from users.models import User
import datetime




class Category(models.Model):
    name = models.CharField(max_length=80, default='', blank = False)

    def __str__(self):
        return self.name

class Product(models.Model):
    people_img = models.ImageField(upload_to='products', null=True)
    upper_img = models.ImageField(upload_to='products', null=True)
    lower_image = models.ImageField(upload_to='products', null=True)
    brand = models.CharField(max_length=80, null=True)
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    frame_color = models.CharField(max_length=100, null=True)
    frame_material = models.CharField(max_length=100, null=True)
    frame_treatment = models.CharField(max_length=100, null=True)
    frame_shape = models.CharField(max_length=100, null=True)
    lens_color = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    slug = models.SlugField()
    

    

    def __str__(self):
        return self.name
    


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=100, default='', blank = True)
    phone = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

  
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default = True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null = True)
    order_date = models.DateField(default = datetime.datetime.today)
    

    


    


