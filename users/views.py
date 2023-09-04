from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from . forms import UserRegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ecomWeb.forms import BillingAddressForm
from . forms import BillingModelForm, UpdateProfile, UpdateUser
from . models import BillingAdress, Wishlist
from ecomWeb.models import Order, OrderItem,Product
# Create your views here.

@login_required(login_url = 'login')
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        billing_form = BillingModelForm(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request, f'Profile Updated')
            return redirect ('profile')
        elif billing_form.is_valid():
            billing_form.save()
            messages.success(request,f'Billing Address added' )
            return redirect('profile')
    else:
        form = ProfileForm()
        billing_form = BillingModelForm()
    return render(request, 'users/profile/profile.html', {'form' : form, 'billing_form' : billing_form})

@login_required(login_url = 'login')
def billing(request):
    if request.method == 'POST':
        billing_form = BillingModelForm(request.POST, instance = request.user)
       
        if billing_form.is_valid():
            billing_form.save()
            messages.success(request,f'Billing Address added' )
            return redirect('profile')
    else:
        billing_form = BillingModelForm(instance=request.user)
    return render(request, 'users/profile/billing.html',  {'billing_form' : billing_form, 'billing' : BillingAdress.objects.all()})

@login_required(login_url='login')
def editprofile(request):
    if request.method == 'POST':
        userUpdate = UpdateUser(request.POST, instance = request.user)
        profileUpdate = UpdateProfile(request.POST, request.FILES,instance = request.user.profile)

        if userUpdate.is_valid() and profileUpdate.is_valid():
            userUpdate.save()
            profileUpdate.save()
            messages.success(request, f'Profile Updated Successully')
            return redirect('profile')
    else :
        userUpdate = UpdateUser()
        profileUpdate = UpdateProfile()

    context = {
        'userupdateform' : userUpdate,
        'profileupdateform' : profileUpdate
    }
    return render(request, 'users/editProfile.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been sucessfully registererd.')
            return redirect('login')
        
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required(login_url = 'login')
def myorder(request):

    return render(request, 'users/profile/order.html', {"orders" : Order.objects.filter(user = request.user).order_by('id'), 'orderitems' : OrderItem.objects.all() })


def wishlist(request, id):
    product = Product.objects.get(id = id)
    user = request.user
    if request.user.is_authenticated:
        if product.include_offer:
            product.price = product.discount_price
            product.save()
            Wishlist.objects.get_or_create(user = user, product = product)

        else:
            Wishlist.objects.get_or_create(user = user, product = product)

        messages.success(request, "Added to Wishlist!")
    else: 
        messages.error(request, f"You have to login in order to add items in cart.")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def mywishlist(request):
    user = request.user
    return render(request, 'users/profile/wishlist.html', {'wishlists' : Wishlist.objects.filter(user= user)})

def remove_wishlist(request, id):
    try:
        wishlist = Wishlist.objects.get(id = id)
        wishlist.delete()
    except Exception as e:
        print(e)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
