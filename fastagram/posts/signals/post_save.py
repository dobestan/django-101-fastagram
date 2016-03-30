from django.db.models.signals import post_save
from django.dispatch import receiver

from posts.models import Post
from tags.models import Tag


@receiver(post_save, sender=Post)
def post_save_post(sender, instance, created, **kwargs):
    if not instance.hash_id:
        instance.init_hash_id()


@receiver(post_save, sender=Post)
def post_save_post_tags(sender, instance, created, **kwargs):
    from tags.utils.tagify import get_tag_list

    tag_list = get_tag_list(instance.content)

    for tag_name in tag_list:
        tag, is_tag_created = Tag.objects.get_or_create(
            name=tag_name,
        )
        instance.tag_set.add(tag)
