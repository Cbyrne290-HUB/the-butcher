"""
Automated tests for The Butcher restaurant booking system.
Covers models, forms, and views for both Booking and Review.
"""

import datetime
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Booking, Review, TIME_SLOTS
from .forms import BookingForm, ReviewForm


# ===================================================================
# Model tests
# ===================================================================

class BookingModelTest(TestCase):
    """Tests for the Booking model."""

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        self.booking = Booking.objects.create(
            user=self.user,
            date=self.tomorrow,
            time_slot='19:00',
            party_size=2,
            status=Booking.STATUS_PENDING
        )

    def test_booking_str(self):
        """Booking __str__ includes user email and date."""
        self.assertIn(self.user.email, str(self.booking))
        self.assertIn(str(self.tomorrow), str(self.booking))

    def test_booking_is_upcoming(self):
        """is_upcoming returns True for future bookings."""
        self.assertTrue(self.booking.is_upcoming())

    def test_booking_past_is_not_upcoming(self):
        """is_upcoming returns False for past bookings."""
        past_booking = Booking.objects.create(
            user=self.user,
            date=datetime.date(2020, 1, 1),
            time_slot='12:00',
            party_size=1,
        )
        self.assertFalse(past_booking.is_upcoming())

    def test_default_status_is_pending(self):
        """A new booking defaults to pending status."""
        self.assertEqual(self.booking.status, Booking.STATUS_PENDING)

    def test_get_time_display_label(self):
        """get_time_display_label returns the human-readable time."""
        label = self.booking.get_time_display_label()
        self.assertIn('PM', label)

    def test_booking_ordering(self):
        """Bookings are ordered by date then time_slot."""
        b2 = Booking.objects.create(
            user=self.user,
            date=self.tomorrow + datetime.timedelta(days=1),
            time_slot='12:00',
            party_size=1,
        )
        bookings = list(Booking.objects.filter(user=self.user))
        self.assertEqual(bookings[0].id, self.booking.id)
        self.assertEqual(bookings[1].id, b2.id)


class ReviewModelTest(TestCase):
    """Tests for the Review model."""

    def setUp(self):
        self.user = User.objects.create_user(
            username='reviewer',
            email='reviewer@example.com',
            password='testpass123'
        )
        self.review = Review.objects.create(
            user=self.user,
            rating=5,
            title='Outstanding steak',
            comment='Best ribeye I have ever had.',
            approved=False
        )

    def test_review_str(self):
        """Review __str__ includes user email and rating."""
        self.assertIn(self.user.email, str(self.review))
        self.assertIn('5', str(self.review))

    def test_review_not_approved_by_default(self):
        """Reviews are not approved by default."""
        self.assertFalse(self.review.approved)

    def test_review_approval(self):
        """Setting approved=True persists correctly."""
        self.review.approved = True
        self.review.save()
        self.review.refresh_from_db()
        self.assertTrue(self.review.approved)


# ===================================================================
# Form tests
# ===================================================================

class BookingFormTest(TestCase):
    """Tests for BookingForm validation."""

    def test_valid_form(self):
        """A correctly filled form is valid."""
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        # Skip Tuesdays for the test
        if tomorrow.weekday() == 1:
            tomorrow += datetime.timedelta(days=1)
        form = BookingForm(data={
            'date': tomorrow.isoformat(),
            'time_slot': '19:00',
            'party_size': 2,
            'special_requests': '',
        })
        self.assertTrue(form.is_valid(), form.errors)

    def test_past_date_is_invalid(self):
        """A booking date in the past should fail validation."""
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        form = BookingForm(data={
            'date': yesterday.isoformat(),
            'time_slot': '19:00',
            'party_size': 2,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors)

    def test_tuesday_is_invalid(self):
        """Bookings on Tuesdays (closed day) should fail validation."""
        # Find the next Tuesday
        today = datetime.date.today()
        days_ahead = (1 - today.weekday()) % 7 or 7  # 1 = Tuesday
        next_tuesday = today + datetime.timedelta(days=days_ahead)
        form = BookingForm(data={
            'date': next_tuesday.isoformat(),
            'time_slot': '19:00',
            'party_size': 2,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors)

    def test_party_size_zero_is_invalid(self):
        """Party size of 0 is not allowed."""
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        form = BookingForm(data={
            'date': tomorrow.isoformat(),
            'time_slot': '19:00',
            'party_size': 0,
        })
        self.assertFalse(form.is_valid())

    def test_party_size_exceeds_max_is_invalid(self):
        """Party size above 12 is not allowed."""
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        form = BookingForm(data={
            'date': tomorrow.isoformat(),
            'time_slot': '19:00',
            'party_size': 13,
        })
        self.assertFalse(form.is_valid())


class ReviewFormTest(TestCase):
    """Tests for ReviewForm validation."""

    def test_valid_review_form(self):
        """A correctly filled review form is valid."""
        form = ReviewForm(data={
            'rating': 5,
            'title': 'Amazing experience',
            'comment': 'The fillet steak was cooked to perfection.',
        })
        self.assertTrue(form.is_valid(), form.errors)

    def test_missing_comment_is_invalid(self):
        """A review without a comment should be invalid."""
        form = ReviewForm(data={
            'rating': 4,
            'title': 'Great food',
            'comment': '',
        })
        self.assertFalse(form.is_valid())

    def test_missing_title_is_invalid(self):
        """A review without a title should be invalid."""
        form = ReviewForm(data={
            'rating': 4,
            'title': '',
            'comment': 'Lovely atmosphere.',
        })
        self.assertFalse(form.is_valid())


# ===================================================================
# View tests
# ===================================================================

class PublicViewTest(TestCase):
    """Tests for views accessible without authentication."""

    def setUp(self):
        self.client = Client()

    def test_home_page_loads(self):
        """Home page returns 200."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/home.html')

    def test_menu_page_loads(self):
        """Menu page returns 200."""
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/menu.html')

    def test_reviews_page_loads(self):
        """Reviews page returns 200."""
        response = self.client.get(reverse('reviews'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/reviews.html')

    def test_booking_create_redirects_unauthenticated(self):
        """Unauthenticated users are redirected away from booking page."""
        response = self.client.get(reverse('booking_create'))
        self.assertNotEqual(response.status_code, 200)

    def test_my_bookings_redirects_unauthenticated(self):
        """Unauthenticated users are redirected away from my-bookings."""
        response = self.client.get(reverse('my_bookings'))
        self.assertNotEqual(response.status_code, 200)

    def test_staff_bookings_redirects_unauthenticated(self):
        """Unauthenticated users cannot access staff area."""
        response = self.client.get(reverse('staff_bookings'))
        self.assertNotEqual(response.status_code, 200)


class BookingViewTest(TestCase):
    """Tests for booking CRUD views."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='bookinguser',
            email='booking@example.com',
            password='testpass123'
        )
        self.other_user = User.objects.create_user(
            username='otheruser',
            email='other@example.com',
            password='testpass123'
        )
        self.tomorrow = datetime.date.today() + datetime.timedelta(days=2)
        # Ensure it's not a Tuesday
        if self.tomorrow.weekday() == 1:
            self.tomorrow += datetime.timedelta(days=1)

        self.booking = Booking.objects.create(
            user=self.user,
            date=self.tomorrow,
            time_slot='19:00',
            party_size=2,
        )

    def test_authenticated_user_can_view_my_bookings(self):
        """Logged-in user sees their bookings page."""
        self.client.login(email='booking@example.com', password='testpass123')
        response = self.client.get(reverse('my_bookings'))
        self.assertEqual(response.status_code, 200)

    def test_authenticated_user_can_create_booking(self):
        """A POST to booking_create creates a booking and redirects."""
        self.client.login(email='booking@example.com', password='testpass123')
        future_date = self.tomorrow + datetime.timedelta(days=5)
        if future_date.weekday() == 1:
            future_date += datetime.timedelta(days=1)
        response = self.client.post(reverse('booking_create'), {
            'date': future_date.isoformat(),
            'time_slot': '18:00',
            'party_size': 3,
            'special_requests': 'Window seat please',
        })
        self.assertRedirects(response, reverse('my_bookings'))
        self.assertEqual(Booking.objects.filter(user=self.user).count(), 2)

    def test_user_cannot_edit_another_users_booking(self):
        """A user cannot edit a booking that belongs to someone else."""
        self.client.login(email='other@example.com', password='testpass123')
        response = self.client.get(reverse('booking_edit', args=[self.booking.id]))
        self.assertEqual(response.status_code, 403)

    def test_user_can_cancel_own_booking(self):
        """A user can cancel their own booking via POST."""
        self.client.login(email='booking@example.com', password='testpass123')
        response = self.client.post(reverse('booking_cancel', args=[self.booking.id]))
        self.assertRedirects(response, reverse('my_bookings'))
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.status, Booking.STATUS_CANCELLED)

    def test_user_cannot_cancel_another_users_booking(self):
        """A user cannot cancel a booking that belongs to someone else."""
        self.client.login(email='other@example.com', password='testpass123')
        response = self.client.post(reverse('booking_cancel', args=[self.booking.id]))
        self.assertEqual(response.status_code, 403)


class ReviewViewTest(TestCase):
    """Tests for review CRUD views."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='reviewuser',
            email='reviewuser@example.com',
            password='testpass123'
        )

    def test_authenticated_user_can_submit_review(self):
        """A logged-in user can POST a new review."""
        self.client.login(email='reviewuser@example.com', password='testpass123')
        response = self.client.post(reverse('review_create'), {
            'rating': 5,
            'title': 'Absolutely fantastic',
            'comment': 'The dry-aged ribeye was outstanding. Will return!',
        })
        self.assertRedirects(response, reverse('reviews'))
        self.assertEqual(Review.objects.filter(user=self.user).count(), 1)

    def test_unauthenticated_user_cannot_submit_review(self):
        """An unauthenticated user is redirected from review_create."""
        response = self.client.get(reverse('review_create'))
        self.assertNotEqual(response.status_code, 200)

    def test_user_cannot_submit_duplicate_review(self):
        """A user with an existing review is redirected instead of shown the form."""
        Review.objects.create(
            user=self.user,
            rating=4,
            title='Great food',
            comment='Loved it.',
        )
        self.client.login(email='reviewuser@example.com', password='testpass123')
        response = self.client.get(reverse('review_create'))
        self.assertRedirects(response, reverse('reviews'))

    def test_user_can_delete_own_review(self):
        """A user can delete their own review."""
        review = Review.objects.create(
            user=self.user,
            rating=3,
            title='Pretty good',
            comment='Decent steak.',
        )
        self.client.login(email='reviewuser@example.com', password='testpass123')
        response = self.client.post(reverse('review_delete', args=[review.id]))
        self.assertRedirects(response, reverse('reviews'))
        self.assertFalse(Review.objects.filter(id=review.id).exists())


class StaffViewTest(TestCase):
    """Tests for staff-only views."""

    def setUp(self):
        self.client = Client()
        self.regular_user = User.objects.create_user(
            username='regular',
            email='regular@example.com',
            password='testpass123'
        )
        self.staff_user = User.objects.create_user(
            username='staff',
            email='staff@example.com',
            password='testpass123',
            is_staff=True
        )

    def test_regular_user_cannot_access_staff_area(self):
        """A regular user is denied access to the staff bookings page."""
        self.client.login(email='regular@example.com', password='testpass123')
        response = self.client.get(reverse('staff_bookings'))
        self.assertNotEqual(response.status_code, 200)

    def test_staff_user_can_access_staff_area(self):
        """A staff user can access the staff bookings page."""
        self.client.login(email='staff@example.com', password='testpass123')
        response = self.client.get(reverse('staff_bookings'))
        self.assertEqual(response.status_code, 200)

    def test_staff_can_update_booking_status(self):
        """Staff can change a booking's status."""
        booking_user = User.objects.create_user(
            username='guest',
            email='guest@example.com',
            password='testpass123'
        )
        tomorrow = datetime.date.today() + datetime.timedelta(days=3)
        booking = Booking.objects.create(
            user=booking_user,
            date=tomorrow,
            time_slot='19:00',
            party_size=2,
            status=Booking.STATUS_PENDING,
        )
        self.client.login(email='staff@example.com', password='testpass123')
        self.client.post(
            reverse('staff_booking_update_status', args=[booking.id]),
            {'status': Booking.STATUS_CONFIRMED}
        )
        booking.refresh_from_db()
        self.assertEqual(booking.status, Booking.STATUS_CONFIRMED)
