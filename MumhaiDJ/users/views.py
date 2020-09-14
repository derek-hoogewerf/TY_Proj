from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Customer
from .forms import ProfileRegisterForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def userRegister(request):
    if request.user.username:
        messages.success(request, f'You already have a user account!')
        return redirect('site-list')
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST)
        #p_form = ProfileRegisterForm(request.POST, request.FILES)
        if (u_form.is_valid()):
            u_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'User Account Created for {username}!')
            return redirect('profile-create')
    else:
        u_form = UserRegisterForm()
        #p_form = ProfileRegisterForm()
    context = {
        'u_form' : u_form,
        #'p_form' : p_form
    }
    return render(request, 'users/register.html', context);
#Put a login required and force p_form.cleaned_data=current user

@login_required
def profileRegister(request):
    if request.method == 'POST':
        #u_form = UserRegisterForm(request.POST)
        p_form = ProfileRegisterForm(request.POST)
        p_form.instance.username=request.user  
        if (p_form.is_valid()):
            p_form.save()
            #user_type = p_form.cleaned_data.get('user_type')
            username = request.user
            messages.success(request, f'Profile Created for {username}!')
            return redirect('site-list')
    else:
        #u_form = UserRegisterForm()
        p_form = ProfileRegisterForm()
    context = {
        #'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/register_profile.html', context);

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.customer)
        if (p_form.is_valid() and u_form.is_valid()):
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'User/Profile Update for {username}!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.customer)
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html',context)


class CustomerCreateView(CreateView):
    model=Customer
    #fields=['first_name','last_name','password','email','number','dob','gender','econ_name','econ_num']    
    fields=['first_name','last_name','password','email','number','gender','econ_name','econ_num']    