from django.contrib import admin
from .models import Business, QRScan, UserPoints


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'city', 'state', 'has_golden_ticket', 'is_active', 'created_at']
    list_filter = ['category', 'city', 'state', 'has_golden_ticket', 'is_active', 'created_at']
    search_fields = ['name', 'email', 'description', 'city', 'state']
    readonly_fields = ['created_at', 'updated_at', 'qr_code']


@admin.register(QRScan)
class QRScanAdmin(admin.ModelAdmin):
    list_display = ['user', 'business', 'points_earned', 'is_golden_ticket', 'scan_date']
    list_filter = ['business', 'is_golden_ticket', 'scan_date']
    search_fields = ['user__username', 'business__name']
    readonly_fields = ['scan_date']


@admin.register(UserPoints)
class UserPointsAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_points', 'giveaway_entries', 'last_updated']
    list_filter = ['last_updated']
    search_fields = ['user__username']
    readonly_fields = ['last_updated']

