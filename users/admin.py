from django.contrib import admin
from . models import Profile, BillingAdress,Cart, CartItems

admin.site.register(Profile)
admin.site.register(BillingAdress)
admin.site.register(Cart)
admin.site.register(CartItems)