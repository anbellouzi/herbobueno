from django.db import models
from django.contrib.auth.models import User
from vendors.models import Business


class VacationPackage(models.Model):
    DESTINATION_CHOICES = [
        ('caribbean', 'Caribbean'),
        ('europe', 'Europe'),
        ('asia', 'Asia'),
        ('north_america', 'North America'),
        ('south_america', 'South America'),
        ('africa', 'Africa'),
        ('oceania', 'Oceania'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    destination = models.CharField(max_length=50, choices=DESTINATION_CHOICES)
    location = models.CharField(max_length=200)
    duration_days = models.PositiveIntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='vacation_images/')
    includes = models.TextField(help_text="What's included in the package")
    terms_conditions = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class BusinessPrize(models.Model):
    PRIZE_TYPE_CHOICES = [
        ('clothing', 'Clothing'),
        ('paraphernalia', 'Paraphernalia'),
        ('concert_tickets', 'Concert Tickets'),
        ('vip_access', 'VIP Access'),
        ('gift_card', 'Gift Card'),
        ('other', 'Other'),
    ]
    
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    prize_type = models.CharField(max_length=50, choices=PRIZE_TYPE_CHOICES)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='prize_images/')
    quantity_available = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.business.name} - {self.name}"


class Giveaway(models.Model):
    GIVEAWAY_TYPE_CHOICES = [
        ('vacation', 'Vacation Package'),
        ('business_prize', 'Business Prize'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    giveaway_type = models.CharField(max_length=50, choices=GIVEAWAY_TYPE_CHOICES)
    vacation_package = models.ForeignKey(VacationPackage, on_delete=models.CASCADE, null=True, blank=True)
    business_prize = models.ForeignKey(BusinessPrize, on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    max_entries = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    @property
    def is_open(self):
        from django.utils import timezone
        now = timezone.now()
        return self.is_active and self.start_date <= now <= self.end_date


class GiveawayEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    giveaway = models.ForeignKey(Giveaway, on_delete=models.CASCADE)
    entry_date = models.DateTimeField(auto_now_add=True)
    entries_count = models.PositiveIntegerField(default=1)
    
    class Meta:
        unique_together = ['user', 'giveaway']
    
    def __str__(self):
        return f"{self.user.username} - {self.giveaway.title} ({self.entries_count} entries)"


class GiveawayWinner(models.Model):
    giveaway = models.ForeignKey(Giveaway, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    won_date = models.DateTimeField(auto_now_add=True)
    is_claimed = models.BooleanField(default=False)
    claimed_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.giveaway.title}"

