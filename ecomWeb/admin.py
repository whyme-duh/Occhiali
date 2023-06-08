from django.contrib import admin
from . models import Product,Category


# Register your models here.
admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug' : ('name', )}
	list_filter = ["include_offer", "category", "gender" , "size", "brand", "glasses_type", "first_long_product", "last_long_product",]