from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .models import MembershipTier, Membership


def membership_tiers(request):
    """Display all membership tiers"""
    tiers = MembershipTier.objects.filter(is_active=True).order_by('price')
    context = {
        'tiers': tiers,
    }
    return render(request, 'memberships/membership_tiers.html', context)


@login_required
def join_membership(request, tier_id):
    """Join a membership tier"""
    tier = get_object_or_404(MembershipTier, id=tier_id, is_active=True)
    
    # Check if user already has an active membership
    existing_membership = Membership.objects.filter(
        user=request.user,
        status='active'
    ).first()
    
    if existing_membership:
        messages.info(request, 'You already have an active membership.')
        return redirect('my_membership')
    
    # Create new membership
    end_date = timezone.now() + timedelta(days=tier.duration_months * 30)
    membership = Membership.objects.create(
        user=request.user,
        tier=tier,
        end_date=end_date
    )
    
    messages.success(request, f'Welcome to the {tier.name}! Your membership is now active.')
    return redirect('my_membership')


@login_required
def my_membership(request):
    """Display user's current membership"""
    membership = Membership.objects.filter(
        user=request.user,
        status='active'
    ).first()
    
    context = {
        'membership': membership,
    }
    return render(request, 'memberships/my_membership.html', context)


@login_required
def membership_history(request):
    """Display user's membership history"""
    memberships = Membership.objects.filter(user=request.user).order_by('-start_date')
    context = {
        'memberships': memberships,
    }
    return render(request, 'memberships/membership_history.html', context)

