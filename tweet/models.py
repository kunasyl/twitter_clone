from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Tweet(models.Model):
    user = models.ForeignKey(User, related_name='tweets', on_delete=models.CASCADE)
    tweet = models.CharField(max_length=140)
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        # Descending order (newest tweets first)
        ordering = ('-created_at',)
