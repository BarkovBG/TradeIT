from django.conf import settings
from django.db import models


class Notification(models.Model):
    STATE_CHOICES = (
        ('now_shown', 'now_shown'),
        ('shown', 'shown'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    message = models.CharField(max_length=3000)
    state = models.CharField(max_length=300, choices=STATE_CHOICES)

    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)
