from django.contrib import admin
from . models import Product,Category, Order,Cart


# Register your models here.
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Cart)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug' : ('name', )}