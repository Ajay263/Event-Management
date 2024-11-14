from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='event_images/', null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)  # New field
    stop_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class EventRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} registered for {self.event.name}"


class BarcodeScan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    scan_time = models.DateTimeField()
    time_taken = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - Event: {self.event.name} - Scan Time: {self.scan_time}, Time Taken: {self.time_taken} seconds"

    class Meta:
        ordering = ['time_taken']  # Orders by the shortest time taken
        indexes = [
            models.Index(fields=['time_taken']),
        ]


class QRCodeData(models.Model):
    data = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.data


class AboutSection(models.Model):
    subtitle = models.CharField(max_length=255, help_text="Subtitle for the about section")
    description = models.TextField(help_text="Main description of the about section (use paragraphs separated by \\n).")
    image = models.ImageField(upload_to='about_images/', help_text="Upload an image for the about section.")

    def __str__(self):
        return self.description 


class Stat(models.Model):
    about_section = models.ForeignKey(AboutSection, related_name='stats', on_delete=models.CASCADE)
    number = models.CharField(max_length=50, help_text="Stat number (e.g., 300+)")
    text = models.CharField(max_length=100, help_text="Stat description (e.g., 'Participants')")

    def __str__(self):
        return f"{self.number} - {self.text}"
