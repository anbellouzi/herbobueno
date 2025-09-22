from django import forms
from .models import Business


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = [
            'name', 'description', 'category', 'website', 'email', 'phone',
            'address', 'city', 'state', 'zip_code', 'latitude', 'longitude',
            'logo', 'banner_image', 'points_per_visit', 'has_golden_ticket',
            'hours_monday', 'hours_tuesday', 'hours_wednesday', 'hours_thursday',
            'hours_friday', 'hours_saturday', 'hours_sunday'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'address': forms.Textarea(attrs={'rows': 2}),
            'hours_monday': forms.TextInput(attrs={'placeholder': 'e.g., 9:00 AM - 6:00 PM'}),
            'hours_tuesday': forms.TextInput(attrs={'placeholder': 'e.g., 9:00 AM - 6:00 PM'}),
            'hours_wednesday': forms.TextInput(attrs={'placeholder': 'e.g., 9:00 AM - 6:00 PM'}),
            'hours_thursday': forms.TextInput(attrs={'placeholder': 'e.g., 9:00 AM - 6:00 PM'}),
            'hours_friday': forms.TextInput(attrs={'placeholder': 'e.g., 9:00 AM - 6:00 PM'}),
            'hours_saturday': forms.TextInput(attrs={'placeholder': 'e.g., 10:00 AM - 4:00 PM'}),
            'hours_sunday': forms.TextInput(attrs={'placeholder': 'e.g., Closed or 12:00 PM - 5:00 PM'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['points_per_visit'].help_text = 'Points users earn when they scan your QR code (default: 10)'
        self.fields['has_golden_ticket'].help_text = 'Check this if your business has a golden ticket (5x points bonus)'
        self.fields['latitude'].help_text = 'Optional: GPS latitude for location services'
        self.fields['longitude'].help_text = 'Optional: GPS longitude for location services'

