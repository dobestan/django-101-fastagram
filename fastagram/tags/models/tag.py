from django.db import models


class Tag(models.Model):

    name = models.CharField(
        max_length=15,
        unique=True,
    )

    @property
    def full_name(self):
        return "#{tag_name}".format(
            tag_name=self.name,
        )

    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    def __str__(self):
        return self.full_name
