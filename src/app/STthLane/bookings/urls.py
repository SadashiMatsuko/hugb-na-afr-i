from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='bookings-index'),
    path('add_booking/', views.add_bookings, name='add-booking'),
    path('edit_booking/<int:booking_id>', views.edit_booking, name='edit-booking'),
    path('remove_booking/<int:booking_id>', views.remove_booking, name='remove-booking'),
]