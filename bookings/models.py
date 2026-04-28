"""Models for The Butcher restaurant booking system."""

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime


# Available time slots for bookings
TIME_SLOTS = [
    ('12:00', '12:00 PM'),
    ('12:30', '12:30 PM'),
    ('13:00', '1:00 PM'),
    ('13:30', '1:30 PM'),
    ('14:00', '2:00 PM'),
    ('14:30', '2:30 PM'),
    ('17:00', '5:00 PM'),
    ('17:30', '5:30 PM'),
    ('18:00', '6:00 PM'),
    ('18:30', '6:30 PM'),
    ('19:00', '7:00 PM'),
    ('19:30', '7:30 PM'),
    ('20:00', '8:00 PM'),
    ('20:30', '8:30 PM'),
    ('21:00', '9:00 PM'),
    ('21:30', '9:30 PM'),
]


class Booking(models.Model):
    """
    Represents a table booking at The Butcher restaurant.
    Users can create, view, edit and cancel their own bookings.
    Staff can view and manage all bookings.
    """

    STATUS_PENDING = 'pending'
    STATUS_CONFIRMED = 'confirmed'
    STATUS_CANCELLED = 'cancelled'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_CONFIRMED, 'Confirmed'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    date = models.DateField()
    time_slot = models.CharField(max_length=5, choices=TIME_SLOTS)
    party_size = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    special_requests = models.TextField(blank=True, default='')
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date', 'time_slot']

    def __str__(self):
        return (
            f"Booking for {self.user.get_full_name() or self.user.email} "
            f"on {self.date} at {self.time_slot} ({self.party_size} guests)"
        )

    def is_upcoming(self):
        """Returns True if the booking date is today or in the future."""
        return self.date >= datetime.date.today()

    def get_time_display_label(self):
        """Returns the human-readable time label for this booking's time slot."""
        return dict(TIME_SLOTS).get(self.time_slot, self.time_slot)


class Review(models.Model):
    """
    Represents a customer review of The Butcher restaurant.
    Reviews require admin approval before appearing publicly.
    Users can create, edit and delete their own reviews.
    """

    RATING_CHOICES = [(i, f'{i} Star{"s" if i > 1 else ""}') for i in range(1, 6)]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.IntegerField(
        choices=RATING_CHOICES,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    title = models.CharField(max_length=100)
    comment = models.TextField()
    approved = models.BooleanField(
        default=False,
        help_text='Only approved reviews are shown to the public.'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Review by {self.user.email} — {self.rating}/5 stars"
