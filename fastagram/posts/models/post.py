from django.db import models
from django.conf import settings


class Post(models.Model):

    hash_id = models.CharField(
        max_length=8,
        blank=True,
        null=True,
        unique=True,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )
    image = models.ImageField()
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    def init_hash_id(self):
        from hashids import Hashids

        hashids_object = Hashids(salt="dobestan", min_length=4)
        hash_id = hashids_object.encode(self.id)
        self.hash_id = hash_id
        self.save()
