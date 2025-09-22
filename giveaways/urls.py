from django.urls import path
from . import views

urlpatterns = [
    path('', views.giveaway_list, name='giveaway_list'),
    path('<int:giveaway_id>/', views.giveaway_detail, name='giveaway_detail'),
    path('<int:giveaway_id>/enter/', views.enter_giveaway, name='enter_giveaway'),
    path('my-entries/', views.my_entries, name='my_entries'),
    path('vacation-packages/', views.vacation_packages, name='vacation_packages'),
    path('vendor-prizes/', views.vendor_prizes, name='vendor_prizes'),
    path('my-winnings/', views.my_winnings, name='my_winnings'),
]

