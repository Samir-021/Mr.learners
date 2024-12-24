from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class HotelRestro(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def clean(self):
        if not (-90 <= self.latitude <= 90):
            raise ValidationError("Latitude must be between -90 and 90.")
        if not (-180 <= self.longitude <= 180):
            raise ValidationError("Longitude must be between -180 and 180.")

    def get_average_rating(self):
        reviews = self.reviews.all()
        return sum([review.rating for review in reviews]) / len(reviews) if reviews else None

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class FavoriteHotel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    hotel = models.ForeignKey(HotelRestro, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.hotel.name}"
