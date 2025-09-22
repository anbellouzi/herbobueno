from django.urls import path
from . import views

urlpatterns = [
    path('', views.ecosystem_list, name='ecosystem_list'),
    path('business/<int:business_id>/', views.business_detail, name='business_detail'),
    path('business/<int:business_id>/scan/', views.scan_qr_code, name='scan_qr_code'),
    path('signup/', views.business_signup, name='business_signup'),
    path('my-scans/', views.my_scans, name='my_scans'),
    path('golden-tickets/', views.golden_ticket_locations, name='golden_ticket_locations'),
    path('api/nearby/', views.nearby_businesses, name='nearby_businesses'),
]

