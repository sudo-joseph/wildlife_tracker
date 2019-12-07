from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class Report(models.Model):
    """Define Report."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    type = models.CharField(max_length=30)
    long_position = models.DecimalField(max_digits=10, decimal_places=7)
    lat_position = models.DecimalField(max_digits=10, decimal_places=7)
    text = models.CharField(max_length=160)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    image = models.FileField(upload_to='tweet_images/', null=True, blank=True)
