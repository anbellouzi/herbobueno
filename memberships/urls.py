from django.urls import path
from . import views

urlpatterns = [
    path('', views.membership_tiers, name='membership_tiers'),
    path('join/<int:tier_id>/', views.join_membership, name='join_membership'),
    path('my-membership/', views.my_membership, name='my_membership'),
    path('history/', views.membership_history, name='membership_history'),
]

