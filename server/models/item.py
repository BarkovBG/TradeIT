from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Item(models.Model):
    STATE_CHOICES = (
        ('exchanged', 'exchanged'),
        ('exposed', 'exposed'),
        ('draft', 'draft'),
    )
    CATEGORY_CHOICES = (
        ('clothes', 'clothes'),
        ('accessory', 'accessory'),
    )

    photos = ArrayField(models.URLField(), blank=True)
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=3000)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    state = models.CharField(max_length=300, choices=STATE_CHOICES)
    category = models.CharField(max_length=300, choices=CATEGORY_CHOICES)

    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)
