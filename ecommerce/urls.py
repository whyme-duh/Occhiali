"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from ecommerce import settings
from django.conf.urls.static import static  
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ecomWeb.urls')),
    path('login/',auth_views.LoginView.as_view(template_name = 'users/login.html', redirect_authenticated_user= True), name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'users/register.html'), name = 'logout'),
    path('profile/', user_views.profile, name = 'profile'),
    path('profile/billing', user_views.billing, name = 'billing'),
    path('register/', user_views.register, name = 'register'),
    path('edit-profile/', user_views.editprofile, name = 'edit-profile'),
    path('myorder/', user_views.myorder, name = 'myorder'),
    path('wishlist/<int:id>/', user_views.wishlist, name = 'wishlist'),
    path('mywishlist/', user_views.mywishlist, name = 'mywishlist'),
    path('remove_wishlist/<int:id>', user_views.remove_wishlist, name = 'remove_wishlist'),
    
    
]

handler404= 'ecomWeb.views.error_404_view'
handler500 = 'ecomWeb.views.error_500_view'


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
