from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name = "home"),
    path('add-to-cart/<int:id>/', views.add_to_cart, name= 'add-to-cart'),
    path('remove-cart/<id>/', views.remove_cart, name= 'remove-cart'),
    path('delete-cart/', views.delete_cart, name= 'delete-cart'),
    path('cart/add/<int:id>', views.cart_add, name= 'cart-add'),
    path('cart/', views.cart, name = 'cart'),
    path('sunglasses/', views.sunglasses, name = 'sunglasses'),
    path('eyeglasses/', views.eyeglasses, name = 'eyeglasses'),
    path('men/', views.menSunglasses, name = 'men-sunglasses'),
    path('women/', views.womenSunglasses, name = 'women-sunglasses'),
    path('<slug:slug>',views.ProductDetailView.as_view(), name = 'product-detail' ),
    path('payout/', views.payout, name = 'payout'),

]