from django.contrib import admin
from .models import MembershipTier, Membership


@admin.register(MembershipTier)
class MembershipTierAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'duration_months', 'giveaway_multiplier', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at']


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ['user', 'tier', 'status', 'start_date', 'end_date', 'is_active']
    list_filter = ['status', 'tier', 'start_date', 'end_date']
    search_fields = ['user__username', 'tier__name']
    readonly_fields = ['start_date', 'created_at']
