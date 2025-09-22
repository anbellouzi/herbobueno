#!/usr/bin/env python
import os
import sys
import django
from datetime import datetime, timedelta

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'herbo_bueno.settings')
django.setup()

from django.contrib.auth.models import User
from vendors.models import Vendor, VendorProduct
from giveaways.models import VacationPackage, VendorPrize, Giveaway
from memberships.models import MembershipTier

def create_sample_data():
    print("Creating sample data...")
    
    # Create membership tiers
    basic_tier, created = MembershipTier.objects.get_or_create(
        name="Basic",
        defaults={
            'description': 'Perfect for getting started with Herbo Bueno Club',
            'price': 0,
            'duration_months': 12,
            'benefits': '• Access to all vendors\n• Basic giveaway entries\n• Community support',
            'giveaway_multiplier': 1
        }
    )
    
    premium_tier, created = MembershipTier.objects.get_or_create(
        name="Premium",
        defaults={
            'description': 'Enhanced benefits and more giveaway entries',
            'price': 29.99,
            'duration_months': 12,
            'benefits': '• Everything in Basic\n• 2x giveaway entries\n• Early access to new giveaways\n• Priority support',
            'giveaway_multiplier': 2
        }
    )
    
    vip_tier, created = MembershipTier.objects.get_or_create(
        name="VIP",
        defaults={
            'description': 'Ultimate experience with maximum benefits',
            'price': 99.99,
            'duration_months': 12,
            'benefits': '• Everything in Premium\n• 3x giveaway entries\n• VIP events access\n• Exclusive merchandise\n• Personal concierge',
            'giveaway_multiplier': 3
        }
    )
    
    # Create vendors
    vendor1, created = Vendor.objects.get_or_create(
        name="Green Dreams Clothing",
        defaults={
            'description': 'Premium cannabis-inspired clothing and accessories',
            'category': 'clothing',
            'email': 'info@greendreams.com',
            'website': 'https://greendreams.com',
            'phone': '(555) 123-4567'
        }
    )
    
    vendor2, created = Vendor.objects.get_or_create(
        name="Smoke & Mirrors",
        defaults={
            'description': 'High-quality smoking accessories and paraphernalia',
            'category': 'paraphernalia',
            'email': 'sales@smokeandmirrors.com',
            'website': 'https://smokeandmirrors.com',
            'phone': '(555) 234-5678'
        }
    )
    
    vendor3, created = Vendor.objects.get_or_create(
        name="Concert Central",
        defaults={
            'description': 'Exclusive concert tickets and VIP experiences',
            'category': 'entertainment',
            'email': 'tickets@concertcentral.com',
            'website': 'https://concertcentral.com',
            'phone': '(555) 345-6789'
        }
    )
    
    # Create vendor products
    VendorProduct.objects.get_or_create(
        vendor=vendor1,
        name="Cannabis Leaf Hoodie",
        defaults={
            'description': 'Comfortable hoodie with embroidered cannabis leaf design',
            'price': 79.99
        }
    )
    
    VendorProduct.objects.get_or_create(
        vendor=vendor1,
        name="420 T-Shirt",
        defaults={
            'description': 'Classic 420 themed t-shirt in various colors',
            'price': 29.99
        }
    )
    
    VendorProduct.objects.get_or_create(
        vendor=vendor2,
        name="Premium Glass Bong",
        defaults={
            'description': 'Hand-blown glass bong with percolator',
            'price': 199.99
        }
    )
    
    VendorProduct.objects.get_or_create(
        vendor=vendor2,
        name="Rolling Tray Set",
        defaults={
            'description': 'Complete rolling tray with accessories',
            'price': 49.99
        }
    )
    
    # Create vacation packages
    vacation1, created = VacationPackage.objects.get_or_create(
        title="Caribbean Paradise - Jamaica",
        defaults={
            'description': '7-day all-inclusive vacation to beautiful Jamaica with luxury resort accommodations',
            'destination': 'caribbean',
            'location': 'Montego Bay, Jamaica',
            'duration_days': 7,
            'value': 3500.00,
            'includes': '• Round-trip airfare\n• 7 nights luxury resort accommodation\n• All meals and drinks\n• Airport transfers\n• Resort activities and entertainment\n• Spa credit ($200)',
            'terms_conditions': 'Valid for 12 months from win date. Blackout dates apply during peak seasons. Winner responsible for passport and travel insurance.'
        }
    )
    
    vacation2, created = VacationPackage.objects.get_or_create(
        title="European Adventure - Italy",
        defaults={
            'description': '7-day luxury tour of Italy including Rome, Florence, and Venice',
            'destination': 'europe',
            'location': 'Rome, Florence, Venice, Italy',
            'duration_days': 7,
            'value': 4500.00,
            'includes': '• Round-trip airfare\n• 7 nights luxury hotel accommodations\n• Daily breakfast and 3 dinners\n• Private guided tours\n• High-speed train between cities\n• Museum passes',
            'terms_conditions': 'Valid for 18 months from win date. Peak season surcharges may apply. Winner responsible for passport and travel insurance.'
        }
    )
    
    # Create vendor prizes
    VendorPrize.objects.get_or_create(
        vendor=vendor1,
        name="Complete Wardrobe Collection",
        defaults={
            'description': 'Complete collection of cannabis-inspired clothing including hoodies, t-shirts, and accessories',
            'prize_type': 'clothing',
            'value': 500.00,
            'quantity_available': 5
        }
    )
    
    VendorPrize.objects.get_or_create(
        vendor=vendor2,
        name="Premium Smoking Kit",
        defaults={
            'description': 'Complete premium smoking kit with glass bong, rolling tray, and accessories',
            'prize_type': 'paraphernalia',
            'value': 300.00,
            'quantity_available': 10
        }
    )
    
    VendorPrize.objects.get_or_create(
        vendor=vendor3,
        name="VIP Concert Experience",
        defaults={
            'description': 'VIP tickets to exclusive concert with backstage access and meet & greet',
            'prize_type': 'concert_tickets',
            'value': 800.00,
            'quantity_available': 3
        }
    )
    
    # Create giveaways
    giveaway1, created = Giveaway.objects.get_or_create(
        title="Win a 7-Day Jamaica Vacation!",
        defaults={
            'description': 'Enter to win an all-inclusive 7-day vacation to beautiful Jamaica!',
            'giveaway_type': 'vacation',
            'vacation_package': vacation1,
            'start_date': datetime.now(),
            'end_date': datetime.now() + timedelta(days=30)
        }
    )
    
    giveaway2, created = Giveaway.objects.get_or_create(
        title="Win Premium Clothing Collection!",
        defaults={
            'description': 'Enter to win a complete wardrobe collection from Green Dreams Clothing!',
            'giveaway_type': 'vendor_prize',
            'vendor_prize': VendorPrize.objects.filter(vendor=vendor1).first(),
            'start_date': datetime.now(),
            'end_date': datetime.now() + timedelta(days=14)
        }
    )
    
    print("Sample data created successfully!")
    print(f"Created {MembershipTier.objects.count()} membership tiers")
    print(f"Created {Vendor.objects.count()} vendors")
    print(f"Created {VendorProduct.objects.count()} vendor products")
    print(f"Created {VacationPackage.objects.count()} vacation packages")
    print(f"Created {VendorPrize.objects.count()} vendor prizes")
    print(f"Created {Giveaway.objects.count()} giveaways")

if __name__ == '__main__':
    create_sample_data()
