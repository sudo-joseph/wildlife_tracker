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
    # I think type should be int type with type table
    # latlon=models.CharField(max_length=100)
    # address=models.CharField(max_length=1000)
    text = models.CharField(max_length=160)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    image = models.FileField(upload_to='tweet_images/', null=True, blank=True)
