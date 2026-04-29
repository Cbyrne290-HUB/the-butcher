"""Views for The Butcher restaurant booking system."""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Booking, Review
from .forms import BookingForm, ReviewForm


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def is_staff(user):
    """Returns True if the user is a staff member or superuser."""
    return user.is_staff or user.is_superuser


# ---------------------------------------------------------------------------
# Public views
# ---------------------------------------------------------------------------

def home(request):
    """Renders the home page with headline stats and highlights."""
    approved_reviews = Review.objects.filter(approved=True).order_by('-created_at')[:3]
    context = {
        'reviews': approved_reviews,
    }
    return render(request, 'bookings/home.html', context)


def menu(request):
    """Renders the static menu page."""
    return render(request, 'bookings/menu.html')


def reviews_list(request):
    """Displays all approved reviews and a form for logged-in users to submit one."""
    approved_reviews = Review.objects.filter(approved=True).order_by('-created_at')
    user_review = None

    # Check if the logged-in user already has a review (approved or pending)
    if request.user.is_authenticated:
        user_review = Review.objects.filter(user=request.user).first()

    context = {
        'reviews': approved_reviews,
        'user_review': user_review,
    }
    return render(request, 'bookings/reviews.html', context)


# ---------------------------------------------------------------------------
# Booking views (login required)
# ---------------------------------------------------------------------------

@login_required
def booking_create(request):
    """Allows a logged-in user to create a new table booking."""
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.status = Booking.STATUS_PENDING
            booking.save()
            messages.success(
                request,
                f'Your table for {booking.party_size} has been requested for '
                f'{booking.date} at {booking.get_time_display_label()}. '
                'We will confirm shortly!'
            )
            return redirect('my_bookings')
    else:
        form = BookingForm()

    return render(request, 'bookings/booking_form.html', {
        'form': form,
        'title': 'Book a Table',
        'submit_label': 'Request Booking',
    })


@login_required
def my_bookings(request):
    """Displays the logged-in user's upcoming and past bookings."""
    user_bookings = Booking.objects.filter(user=request.user).order_by('-date', '-time_slot')
    import datetime
    today = datetime.date.today()
    upcoming = user_bookings.filter(date__gte=today).exclude(status=Booking.STATUS_CANCELLED)
    past = user_bookings.filter(date__lt=today) | user_bookings.filter(status=Booking.STATUS_CANCELLED)
    past = past.distinct().order_by('-date')

    context = {
        'upcoming': upcoming,
        'past': past,
    }
    return render(request, 'bookings/my_bookings.html', context)


@login_required
def booking_edit(request, booking_id):
    """Allows a user to edit their own pending or confirmed booking."""
    booking = get_object_or_404(Booking, id=booking_id)

    # Only the booking owner can edit it
    if booking.user != request.user:
        return HttpResponseForbidden()

    # Cannot edit a cancelled booking
    if booking.status == Booking.STATUS_CANCELLED:
        messages.error(request, 'Cancelled bookings cannot be edited.')
        return redirect('my_bookings')

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your booking has been updated successfully.'
            )
            return redirect('my_bookings')
    else:
        form = BookingForm(instance=booking)

    return render(request, 'bookings/booking_form.html', {
        'form': form,
        'title': 'Edit Booking',
        'submit_label': 'Save Changes',
        'booking': booking,
    })


@login_required
def booking_cancel(request, booking_id):
    """Allows a user to cancel their own booking via a confirmation page."""
    booking = get_object_or_404(Booking, id=booking_id)

    # Only the booking owner can cancel it
    if booking.user != request.user:
        return HttpResponseForbidden()

    if booking.status == Booking.STATUS_CANCELLED:
        messages.info(request, 'This booking is already cancelled.')
        return redirect('my_bookings')

    if request.method == 'POST':
        booking.status = Booking.STATUS_CANCELLED
        booking.save()
        messages.success(
            request,
            f'Your booking on {booking.date} at {booking.get_time_display_label()} '
            'has been cancelled.'
        )
        return redirect('my_bookings')

    return render(request, 'bookings/booking_cancel.html', {'booking': booking})


# ---------------------------------------------------------------------------
# Review views (login required to write/edit/delete)
# ---------------------------------------------------------------------------

@login_required
def review_create(request):
    """Allows a logged-in user to submit a new review."""
    # Prevent duplicate reviews
    if Review.objects.filter(user=request.user).exists():
        messages.info(request, 'You have already submitted a review. You can edit it below.')
        return redirect('reviews')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.approved = False
            review.save()
            messages.success(
                request,
                'Thank you for your review! It will appear once approved by our team.'
            )
            return redirect('reviews')
    else:
        form = ReviewForm()

    return render(request, 'bookings/review_form.html', {
        'form': form,
        'title': 'Write a Review',
        'submit_label': 'Submit Review',
    })


@login_required
def review_edit(request, review_id):
    """Allows a user to edit their own review."""
    review = get_object_or_404(Review, id=review_id)

    if review.user != request.user:
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            updated = form.save(commit=False)
            # Reset approval when edited so staff can re-check it
            updated.approved = False
            updated.save()
            messages.success(
                request,
                'Your review has been updated and will be re-approved by our team.'
            )
            return redirect('reviews')
    else:
        form = ReviewForm(instance=review)

    return render(request, 'bookings/review_form.html', {
        'form': form,
        'title': 'Edit Your Review',
        'submit_label': 'Update Review',
        'review': review,
    })


@login_required
def review_delete(request, review_id):
    """Allows a user to delete their own review via a confirmation page."""
    review = get_object_or_404(Review, id=review_id)

    if review.user != request.user:
        return HttpResponseForbidden()

    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Your review has been deleted.')
        return redirect('reviews')

    return render(request, 'bookings/review_delete.html', {'review': review})


# ---------------------------------------------------------------------------
# Staff views
# ---------------------------------------------------------------------------

@login_required
@user_passes_test(is_staff, login_url='/')
def staff_bookings(request):
    """Displays all bookings to staff members for management."""
    import datetime
    today = datetime.date.today()
    status_filter = request.GET.get('status', '')
    date_filter = request.GET.get('date', '')

    all_bookings = Booking.objects.select_related('user').order_by('-date', 'time_slot')

    if status_filter:
        all_bookings = all_bookings.filter(status=status_filter)
    if date_filter:
        all_bookings = all_bookings.filter(date=date_filter)

    context = {
        'bookings': all_bookings,
        'status_filter': status_filter,
        'date_filter': date_filter,
        'today': today,
        'status_choices': Booking.STATUS_CHOICES,
    }
    return render(request, 'bookings/staff_bookings.html', context)


@login_required
@user_passes_test(is_staff, login_url='/')
def staff_booking_update_status(request, booking_id):
    """Allows staff to confirm or cancel any booking."""
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Booking.STATUS_CHOICES):
            booking.status = new_status
            booking.save()
            messages.success(
                request,
                f'Booking for {booking.user.get_full_name() or booking.user.email} '
                f'updated to {booking.get_status_display()}.'
            )
    return redirect('staff_bookings')


# ---------------------------------------------------------------------------
# Error handlers
# ---------------------------------------------------------------------------

def error_403(request, exception=None):
    """Renders custom 403 Forbidden page."""
    return render(request, '403.html', status=403)


def error_404(request, exception=None):
    """Renders custom 404 Not Found page."""
    return render(request, '404.html', status=404)


def error_500(request):
    """Renders custom 500 Server Error page."""
    return render(request, '500.html', status=500)
