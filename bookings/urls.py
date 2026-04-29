"""URL patterns for The Butcher bookings app."""

from django.urls import path
from . import views

urlpatterns = [
    # Public
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('reviews/', views.reviews_list, name='reviews'),

    # Bookings (auth required)
    path('book/', views.booking_create, name='booking_create'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('my-bookings/<int:booking_id>/edit/', views.booking_edit, name='booking_edit'),
    path('my-bookings/<int:booking_id>/cancel/', views.booking_cancel, name='booking_cancel'),

    # Reviews (auth required to write)
    path('reviews/new/', views.review_create, name='review_create'),
    path('reviews/<int:review_id>/edit/', views.review_edit, name='review_edit'),
    path('reviews/<int:review_id>/delete/', views.review_delete, name='review_delete'),

    # Staff only
    path('staff/bookings/', views.staff_bookings, name='staff_bookings'),
    path('staff/bookings/<int:booking_id>/status/', views.staff_booking_update_status, name='staff_booking_update_status'),
]
