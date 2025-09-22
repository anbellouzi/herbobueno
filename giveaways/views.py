from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q, Sum
from .models import Giveaway, GiveawayEntry, VacationPackage, BusinessPrize, GiveawayWinner
from vendors.models import QRScan, UserPoints


def giveaway_list(request):
    """Display all active giveaways"""
    now = timezone.now()
    giveaways = Giveaway.objects.filter(
        is_active=True,
        start_date__lte=now,
        end_date__gte=now
    ).order_by('-created_at')
    
    context = {
        'giveaways': giveaways,
    }
    return render(request, 'giveaways/giveaway_list.html', context)


def giveaway_detail(request, giveaway_id):
    """Display giveaway details"""
    giveaway = get_object_or_404(Giveaway, id=giveaway_id)
    
    # Get user's entry if they're logged in
    user_entry = None
    if request.user.is_authenticated:
        try:
            user_entry = GiveawayEntry.objects.get(user=request.user, giveaway=giveaway)
        except GiveawayEntry.DoesNotExist:
            pass
    
    # Get total entries for this giveaway
    total_entries = GiveawayEntry.objects.filter(giveaway=giveaway).aggregate(
        total=Sum('entries_count')
    )['total'] or 0
    
    context = {
        'giveaway': giveaway,
        'user_entry': user_entry,
        'total_entries': total_entries,
    }
    return render(request, 'giveaways/giveaway_detail.html', context)


@login_required
def enter_giveaway(request, giveaway_id):
    """Enter a giveaway"""
    giveaway = get_object_or_404(Giveaway, id=giveaway_id)
    
    if not giveaway.is_open:
        messages.error(request, 'This giveaway is not currently open.')
        return redirect('giveaway_detail', giveaway_id=giveaway_id)
    
    # Check if user has scanned any QR codes
    user_scans = QRScan.objects.filter(user=request.user)
    if not user_scans.exists():
        messages.error(request, 'You must scan QR codes from our businesses to enter giveaways.')
        return redirect('ecosystem_list')
    
    # Get or create user's entry
    entry, created = GiveawayEntry.objects.get_or_create(
        user=request.user,
        giveaway=giveaway,
        defaults={'entries_count': 1}
    )
    
    if not created:
        # User already has an entry, add more entries based on points
        user_points = UserPoints.objects.filter(user=request.user).first()
        if user_points:
            entry.entries_count = user_points.giveaway_entries
            entry.save()
            messages.success(request, f'Your giveaway entries have been updated to {entry.entries_count}.')
    else:
        messages.success(request, 'You have successfully entered the giveaway!')
    
    return redirect('giveaway_detail', giveaway_id=giveaway_id)


@login_required
def my_entries(request):
    """Display user's giveaway entries"""
    entries = GiveawayEntry.objects.filter(user=request.user).order_by('-entry_date')
    context = {
        'entries': entries,
    }
    return render(request, 'giveaways/my_entries.html', context)


def vacation_packages(request):
    """Display all vacation packages"""
    packages = VacationPackage.objects.filter(is_active=True)
    context = {
        'packages': packages,
    }
    return render(request, 'giveaways/vacation_packages.html', context)


def vendor_prizes(request):
    """Display all vendor prizes"""
    prizes = VendorPrize.objects.filter(is_active=True, quantity_available__gt=0)
    context = {
        'prizes': prizes,
    }
    return render(request, 'giveaways/vendor_prizes.html', context)


@login_required
def my_winnings(request):
    """Display user's winnings"""
    winnings = GiveawayWinner.objects.filter(user=request.user).order_by('-won_date')
    context = {
        'winnings': winnings,
    }
    return render(request, 'giveaways/my_winnings.html', context)

