"""Admin configuration for The Butcher booking system."""

from django.contrib import admin
from .models import Booking, Review


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Admin view for managing table bookings."""
    list_display = ('user', 'date', 'time_slot', 'party_size', 'status', 'created_at')
    list_filter = ('status', 'date')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')
    ordering = ('-date', 'time_slot')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('status',)
    date_hierarchy = 'date'

    fieldsets = (
        ('Booking Details', {
            'fields': ('user', 'date', 'time_slot', 'party_size', 'special_requests')
        }),
        ('Status', {
            'fields': ('status',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Admin view for managing customer reviews."""
    list_display = ('user', 'title', 'rating', 'approved', 'created_at')
    list_filter = ('approved', 'rating')
    search_fields = ('user__email', 'title', 'comment')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('approved',)

    actions = ['approve_reviews']

    @admin.action(description='Approve selected reviews')
    def approve_reviews(self, request, queryset):
        """Bulk-approve selected reviews."""
        updated = queryset.update(approved=True)
        self.message_user(request, f'{updated} review(s) approved successfully.')
