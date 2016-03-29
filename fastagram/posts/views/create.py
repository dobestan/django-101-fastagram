from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from posts.models import Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        'content',
        'image',
    ]
    template_name = "posts/create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)
