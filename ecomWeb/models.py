from django.db import models
from PIL import Image
import datetime




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
    



  
    




    


    


