from django.shortcuts import render, redirect
from . forms import UserRegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Profile Updated')
            return redirect ('profile')
    else:
        form = ProfileForm()
    return render(request, 'users/profile.html', {'form' : form})



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



