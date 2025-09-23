from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('golden-ticket/', views.golden_ticket, name='golden_ticket'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
]

