from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ProfileUpdateForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


@login_required
def profile(request):
    template_name = 'accounts/profile.html'
    context = {

    }
    return render(request, template_name, context)

def register(request):
    if request.user.is_authenticated:
        return redirect('blog:home')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created, Login!')
            return redirect('login')
    template_name = 'accounts/register.html'
    form = UserRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, template_name, context)

@login_required
def profile_update(request, pk):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            user_form.save()
            
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
    
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': user_form,
        'p_form': profile_form
    }
    template_name = 'accounts/profile_update.html'
    return render(request, template_name, context)