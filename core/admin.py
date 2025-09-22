from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'city', 'state', 'created_at']
    list_filter = ['city', 'state', 'created_at']
    search_fields = ['user__username', 'user__email', 'phone_number', 'city']
    readonly_fields = ['created_at', 'updated_at']

