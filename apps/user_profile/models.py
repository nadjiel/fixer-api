from django.db import models

from django.conf import settings

USER_MODEL_STRING = settings.AUTH_USER_MODEL


# Add your own custom User fields here. It's safer than overriding Django's
# AUTH_USER_MODEL, especially if you've already migrated the django.contrib.auth
# app (usually the first time you run migrate)


class UserProfile(models.Model):
    owner = models.OneToOneField(
        USER_MODEL_STRING, on_delete=models.CASCADE, related_name="profile"
    )
    phone = models.CharField(max_length=13, blank=True, null=True)
    picture = models.ImageField(upload_to="profile_pictures/", blank=True, null=True)
