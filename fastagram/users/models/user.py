from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    description = models.TextField()

    # follower_set = models.ManyToManyField(
    #     "User",
    #     related_name="followee_set",
    # )

    follower_set = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="followee_set",
        through="Follow",
        through_fields=("followee", "follower"),
    )
