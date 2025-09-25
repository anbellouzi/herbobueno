from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm, CustomUserCreationForm


def home(request):
    """Home page view"""
    return render(request, 'core/home.html')


def about(request):
    """About page view"""
    return render(request, 'core/about.html')


def contact(request):
    """Contact page view"""
    return render(request, 'core/contact.html')


def golden_ticket(request):
    """Golden Ticket info page"""
    return render(request, 'core/golden_ticket.html')


def signup(request):
    """User registration view"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create user profile
            UserProfile.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Account created successfully! Welcome to Herbo Bueno!')
            return redirect('giveaway_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/signup.html', {'form': form})


@login_required
def profile(request):
    """User profile view"""
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    
    return render(request, 'core/profile.html', {'form': form, 'profile': profile})

