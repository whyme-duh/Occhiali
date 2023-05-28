from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
# Create your models here.

class Profile(models.Model):
    image = models.ImageField(upload_to='profile', default='default.jpg')
    user = models.OneToOneField(User, on_delete= models.CASCADE, default=True)
    
    def __str__(self):
        return self.user.username