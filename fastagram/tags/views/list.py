from django.views.generic import ListView

from tags.models import Tag


class TagListView(ListView):
    model = Tag
    template_name = "tags/list.html"
    context_object_name = "tags"
