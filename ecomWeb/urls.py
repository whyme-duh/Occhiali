from django.urls import path, include
from . import views

urlpatterns= [
    path('', views.index, name = "home"),
    path('add-to-cart/<int:id>/', views.add_to_cart, name= 'add-to-cart'),
    path('buy/<int:id>/', views.buynow, name= 'buy-now'),
    path('remove-cart/<int:id>/', views.remove_cart, name= 'remove-cart'),
    path('delete-cart/', views.delete_cart, name= 'delete-cart'),
    path('cart/', views.cart, name = 'cart'),
    path('placeorder/', views.placeorder, name = 'placeorder'),
    path('sunglasses/', views.sunglasses, name = 'sunglasses'),
    path('eyeglasses/', views.eyeglasses, name = 'eyeglasses'),
    path('men/', views.menSunglasses, name = 'men-sunglasses'),
    path('women/', views.womenSunglasses, name = 'women-sunglasses'),
    path('products/<slug:slug>',views.detailpage, name = 'product-detail' ),
    path('payout/', views.payout, name = 'payout'),
    path('buypayout/', views.buypayout, name = 'buy-payout'),
    path('offers/', views.offers, name = 'offers'),
    path('services/', views.services, name = 'services'),
    path('make_payment/', views.make_payment, name='initiate_payment'),
    path('esewa_payment/', views.esewa_payment, name='esewa_payment'),

    path('cancel-order/<int:id>/', views.cancel_order, name= 'cancel-order'),
    path('success-payment/', views.payment_sucess, name='sucess')


]