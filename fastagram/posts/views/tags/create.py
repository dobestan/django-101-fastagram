from django.views.generic import View
from django.shortcuts import redirect

from posts.models import Post
from tags.models import Tag


class PostTagCreateView(View):

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(
            hash_id=self.kwargs.get('slug'),
        )
        tag, is_tag_created = Tag.objects.get_or_create(
            name=request.POST.get('name'),
        )
        post.tag_set.add(tag)

        return redirect(post)
