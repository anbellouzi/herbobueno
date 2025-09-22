from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.utils import timezone
from .models import Business, QRScan, UserPoints
from .forms import BusinessForm


def ecosystem_list(request):
    """Display all active businesses in the ecosystem"""
    businesses = Business.objects.filter(is_active=True)
    category = request.GET.get('category')
    city = request.GET.get('city')
    
    if category:
        businesses = businesses.filter(category=category)
    
    if city:
        businesses = businesses.filter(city__icontains=city)
    
    search_query = request.GET.get('search')
    if search_query:
        businesses = businesses.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query) |
            Q(city__icontains=search_query)
        )
    
    # Get unique cities for filter
    cities = Business.objects.filter(is_active=True).values_list('city', flat=True).distinct().order_by('city')
    
    context = {
        'businesses': businesses,
        'categories': Business.CATEGORY_CHOICES,
        'selected_category': category,
        'selected_city': city,
        'cities': cities,
        'search_query': search_query,
    }
    return render(request, 'vendors/ecosystem_list.html', context)


def business_detail(request, business_id):
    """Display business details and QR code"""
    business = get_object_or_404(Business, id=business_id, is_active=True)
    
    # Get user's scan history for this business
    user_scans = []
    if request.user.is_authenticated:
        user_scans = QRScan.objects.filter(user=request.user, business=business).order_by('-scan_date')
    
    context = {
        'business': business,
        'user_scans': user_scans,
    }
    return render(request, 'vendors/business_detail.html', context)


@login_required
def scan_qr_code(request, business_id):
    """Handle QR code scanning"""
    business = get_object_or_404(Business, id=business_id, is_active=True)
    
    if request.method == 'POST':
        # Check if user already scanned today
        today = timezone.now().date()
        existing_scan = QRScan.objects.filter(
            user=request.user,
            business=business,
            scan_date__date=today
        ).exists()
        
        if existing_scan:
            messages.warning(request, 'You have already scanned this QR code today!')
            return redirect('business_detail', business_id=business_id)
        
        # Calculate points
        points_earned = business.points_per_visit
        is_golden_ticket = business.has_golden_ticket
        
        # Bonus points for golden ticket
        if is_golden_ticket:
            points_earned *= 5  # 5x points for golden ticket locations
            messages.success(request, f'🎉 GOLDEN TICKET! You earned {points_earned} points!')
        else:
            messages.success(request, f'QR code scanned! You earned {points_earned} points!')
        
        # Create scan record
        QRScan.objects.create(
            user=request.user,
            business=business,
            points_earned=points_earned,
            is_golden_ticket=is_golden_ticket
        )
        
        # Update user points
        user_points, created = UserPoints.objects.get_or_create(user=request.user)
        user_points.add_points(points_earned)
        
        return redirect('business_detail', business_id=business_id)
    
    return redirect('business_detail', business_id=business_id)


@login_required
def business_signup(request):
    """Business registration form"""
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save()
            messages.success(request, 'Business application submitted successfully!')
            return redirect('ecosystem_list')
    else:
        form = BusinessForm()
    
    return render(request, 'vendors/business_signup.html', {'form': form})


@login_required
def my_scans(request):
    """Display user's QR scan history and points"""
    scans = QRScan.objects.filter(user=request.user).order_by('-scan_date')
    user_points = UserPoints.objects.filter(user=request.user).first()
    
    context = {
        'scans': scans,
        'user_points': user_points,
    }
    return render(request, 'vendors/my_scans.html', context)


@login_required
def golden_ticket_locations(request):
    """Display businesses with golden tickets"""
    golden_businesses = Business.objects.filter(is_active=True, has_golden_ticket=True)
    
    context = {
        'golden_businesses': golden_businesses,
    }
    return render(request, 'vendors/golden_ticket_locations.html', context)


def nearby_businesses(request):
    """API endpoint for nearby businesses (for future mobile app integration)"""
    if request.method == 'GET':
        lat = request.GET.get('lat')
        lng = request.GET.get('lng')
        radius = request.GET.get('radius', 10)  # Default 10 miles
        
        if lat and lng:
            # This would require a more sophisticated geolocation query
            # For now, return all businesses
            businesses = Business.objects.filter(is_active=True)
            business_data = []
            for business in businesses:
                business_data.append({
                    'id': business.id,
                    'name': business.name,
                    'address': business.full_address,
                    'category': business.get_category_display(),
                    'has_golden_ticket': business.has_golden_ticket,
                    'points_per_visit': business.points_per_visit,
                })
            return JsonResponse({'businesses': business_data})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

