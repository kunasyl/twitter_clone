from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


# Creates user profile as soon as User is created (when signing up, use this)
User.userprofile = property(lambda self: UserProfile.objects.get_or_create(user=self)[0])

