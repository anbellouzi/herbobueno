from django.db import models
from django.contrib.auth.models import User
import uuid


class Business(models.Model):
    CATEGORY_CHOICES = [
        ('clothing', 'Clothing & Fashion'),
        ('paraphernalia', 'Paraphernalia & Accessories'),
        ('entertainment', 'Entertainment & Events'),
        ('food', 'Food & Beverage'),
        ('wellness', 'Wellness & Health'),
        ('retail', 'Retail & Shopping'),
        ('services', 'Services'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    website = models.URLField(blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    
    # Location Information
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    
    # Visual Assets
    logo = models.ImageField(upload_to='business_logos/', blank=True, null=True)
    banner_image = models.ImageField(upload_to='business_banners/', blank=True, null=True)
    
    # QR Code and Points
    qr_code = models.CharField(max_length=100, unique=True, default=uuid.uuid4)
    points_per_visit = models.PositiveIntegerField(default=10)
    has_golden_ticket = models.BooleanField(default=False)
    
    # Business Hours
    hours_monday = models.CharField(max_length=50, blank=True)
    hours_tuesday = models.CharField(max_length=50, blank=True)
    hours_wednesday = models.CharField(max_length=50, blank=True)
    hours_thursday = models.CharField(max_length=50, blank=True)
    hours_friday = models.CharField(max_length=50, blank=True)
    hours_saturday = models.CharField(max_length=50, blank=True)
    hours_sunday = models.CharField(max_length=50, blank=True)
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    @property
    def full_address(self):
        return f"{self.address}, {self.city}, {self.state} {self.zip_code}"


class QRScan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    points_earned = models.PositiveIntegerField()
    scan_date = models.DateTimeField(auto_now_add=True)
    is_golden_ticket = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ['user', 'business', 'scan_date']
    
    def __str__(self):
        return f"{self.user.username} - {self.business.name} - {self.points_earned} points"


class UserPoints(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_points = models.PositiveIntegerField(default=0)
    giveaway_entries = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.total_points} points"
    
    def add_points(self, points):
        self.total_points += points
        # Convert points to giveaway entries (10 points = 1 entry)
        self.giveaway_entries = self.total_points // 10
        self.save()

