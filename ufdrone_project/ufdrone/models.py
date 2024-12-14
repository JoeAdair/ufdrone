from django.db import models

class DroneSighting(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True)  # New field for address
    description = models.TextField(blank=True)
    image_link = models.URLField(max_length=200, blank=True)
    video_link = models.URLField(max_length=200, blank=True)
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city}, {self.state} ({self.date_reported})"
