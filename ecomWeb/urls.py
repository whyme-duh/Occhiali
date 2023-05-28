from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name = "home"),
    path('cart/add/<int:id>', views.cart_add, name= 'cart-add'),
    path('cart/item-clear/<int:id>', views.item_clear, name= 'item-clear'),
    path('cart/', views.cart, name = 'cart'),
    path('category/', views.category, name = 'category'),
    path('<slug:slug>',views.ProductDetailView.as_view(), name = 'product-detail' ),
    path('payout/', views.payout, name = 'payout'),

]