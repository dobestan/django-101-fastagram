from django.db import models
from django.conf import settings


class Follow(models.Model):

    follower = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="+",
    )
    followee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="+",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
