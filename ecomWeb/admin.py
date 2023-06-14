from django.contrib import admin
from . models import Product,Category,Order, OrderItem,Cart,CartItems


# Register your models here.
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.register(Order)
admin.site.register(OrderItem)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug' : ('name', )}
	list_filter = ["include_offer", "category", "gender" , "size", "brand", "glasses_type", "first_long_product", "last_long_product",]