from django.contrib import admin
from .models import VacationPackage, BusinessPrize, Giveaway, GiveawayEntry, GiveawayWinner


@admin.register(VacationPackage)
class VacationPackageAdmin(admin.ModelAdmin):
    list_display = ['title', 'destination', 'location', 'value', 'duration_days', 'is_active']
    list_filter = ['destination', 'is_active', 'created_at']
    search_fields = ['title', 'location', 'description']
    readonly_fields = ['created_at']


@admin.register(BusinessPrize)
class BusinessPrizeAdmin(admin.ModelAdmin):
    list_display = ['name', 'business', 'prize_type', 'value', 'quantity_available', 'is_active']
    list_filter = ['prize_type', 'business', 'is_active', 'created_at']
    search_fields = ['name', 'business__name', 'description']
    readonly_fields = ['created_at']


@admin.register(Giveaway)
class GiveawayAdmin(admin.ModelAdmin):
    list_display = ['title', 'giveaway_type', 'start_date', 'end_date', 'is_active']
    list_filter = ['giveaway_type', 'is_active', 'start_date', 'end_date']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at']


@admin.register(GiveawayEntry)
class GiveawayEntryAdmin(admin.ModelAdmin):
    list_display = ['user', 'giveaway', 'entries_count', 'entry_date']
    list_filter = ['giveaway', 'entry_date']
    search_fields = ['user__username', 'giveaway__title']
    readonly_fields = ['entry_date']


@admin.register(GiveawayWinner)
class GiveawayWinnerAdmin(admin.ModelAdmin):
    list_display = ['user', 'giveaway', 'won_date', 'is_claimed']
    list_filter = ['is_claimed', 'won_date']
    search_fields = ['user__username', 'giveaway__title']
    readonly_fields = ['won_date']
