from email import message
from django.core.exceptions import ValidationError
from typing import override
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
import uuid
class Listing(models.Model):
    listing_id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True, editable=False)
    host_id = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @override
    def __str__(self) -> str:
        return f"Listing {self.listing_id}"

class Booking(models.Model):
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True, editable=False)
    user_id = models.UUIDField(default=uuid.uuid4)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=12, decimal_places=2)

    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        CONFIRMED = 'confirmed', 'Confirmed'
        CANCELLED = 'cancelled', 'Cancelled'
    
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    listing = models.ForeignKey(
        Listing,
        on_delete = models.CASCADE,
        related_name = "bookings"
    )

    @override
    def __str__(self) -> str:
        return f"Booking: {self.booking_id}"

# Review
# review_id: Primary Key, UUID, Indexed
# property_id: Foreign Key, references Property(property_id)
# user_id: Foreign Key, references User(user_id)
# rating: INTEGER, CHECK: rating >= 1 AND rating <= 5, NOT NULL
# comment: TEXT, NOT NULL
# created_at: TIMESTAMP, DEFAULT CURRENT_TIMESTAMP

class Review(models.Model):
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True, editable=False)
    user_id = models.UUIDField(default=uuid.uuid4)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1, message="Rating cannot be less than 1"),
            MaxValueValidator(5, message="Rating cannot be more than 5")
        ]
    )
    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        related_name="review"
    )

    def clean(self):
        if self.rating < 1 or self.rating > 5:
            raise ValidationError({'rating': 'Rating must be between 1 and 5'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    @override
    def __str__(self) -> str:
        return f"Review : {self.review_id}"