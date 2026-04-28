"""Forms for The Butcher restaurant booking system."""

import datetime
from django import forms
from django.core.exceptions import ValidationError
from .models import Booking, Review, TIME_SLOTS


class BookingForm(forms.ModelForm):
    """Form for creating and editing a table booking."""

    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'min': datetime.date.today().isoformat(),
        }),
        help_text='We are open Wednesday to Monday. Closed on Tuesdays.'
    )
    time_slot = forms.ChoiceField(
        choices=TIME_SLOTS,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Preferred Time'
    )
    party_size = forms.IntegerField(
        min_value=1,
        max_value=12,
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label='Number of Guests',
        help_text='We can accommodate groups of 1–12. For larger parties please call us.'
    )
    special_requests = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Allergies, dietary requirements, high chair needed, etc.',
        }),
        label='Special Requests (optional)'
    )

    class Meta:
        model = Booking
        fields = ['date', 'time_slot', 'party_size', 'special_requests']

    def clean_date(self):
        """Validate that the booking date is today or in the future and not a Tuesday."""
        date = self.cleaned_data.get('date')
        if date is None:
            raise ValidationError('Please enter a valid date.')
        if date < datetime.date.today():
            raise ValidationError('Booking date cannot be in the past.')
        # 1 = Tuesday (Monday=0)
        if date.weekday() == 1:
            raise ValidationError(
                'We are closed on Tuesdays. Please choose another day.'
            )
        return date


class ReviewForm(forms.ModelForm):
    """Form for creating and editing a review."""

    rating = forms.ChoiceField(
        choices=[(i, f'{i} Star{"s" if i > 1 else ""}') for i in range(1, 6)],
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Your Rating'
    )
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Summarise your experience in a few words',
        }),
        label='Review Title'
    )
    comment = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Tell us about your visit — the food, the atmosphere, the service…',
        }),
        label='Your Review'
    )

    class Meta:
        model = Review
        fields = ['rating', 'title', 'comment']
