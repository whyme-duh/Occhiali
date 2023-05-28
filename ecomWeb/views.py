from django.shortcuts import render, redirect
from . models import Product,Cart,Category
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from cart.cart import Cart as C
from django.contrib import messages
from . forms import BillingAddressForm, CouponForm, CardForm


# Create your views here.
def index(request):
    return render(request, 'ecomWeb/home.html', {'products':Product.objects.all()})




def cart_add(request,id):
    cart =  C(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    messages.success(request, f'Added to cart')
    return redirect('home')


def item_clear(request, id):
    cart = C(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect('cart')
                




def category(request):
    return render(request, 'ecomWeb/categories.html', {'category':Category.objects.all()})

def cart(request):
    if request.method == 'POST':
        form = CouponForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']

            if code == "ritik":
                messages.success(request, f'Code matched')
            else:
                messages.warning(request, f'Code did not matched.')

            return redirect('cart')
    else:
        form =CouponForm()
    return render(request, 'ecomWeb/cart.html', {'form' : form, 'carts': Cart.objects.all()})


class ProductDetailView(DetailView):
    template_name = 'ecomWeb/detail-page.html'
    model = Product


def payout(request):
    if request.method == 'POST':
        form = BillingAddressForm(request.POST)
        paymentForm = CardForm(request.POST)
        if form.is_vald() or paymentForm.is_valid:
            form.save()
            paymentForm.save()
            messages.success('Payment Done, wait for shipping')
            return redirect('home')
    else:
        form = BillingAddressForm()
        paymentForm = CardForm()
    return render(request, 'ecomWeb/payout/payout.html', {'form': form, 'paymentForm' : paymentForm})

