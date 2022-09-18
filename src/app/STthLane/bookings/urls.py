from django.urls import path
from . import views

urlpatterns = [
    path('add_booking/', views.add_bookings, name='add-booking'),
]