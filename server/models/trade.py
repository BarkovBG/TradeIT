from django.db import models


class Trade(models.Model):
    STATE_CHOICES = (
        ('created', 'created'),
        ('accepted', 'accepted'),
        ('not_accepted', 'not_accepted'),
    )

    item1 = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='item1')
    item2 = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='item2')

    state = models.CharField(max_length=300, choices=STATE_CHOICES)

    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)
