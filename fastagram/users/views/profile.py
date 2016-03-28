from django.views.generic import DetailView
from django.contrib.auth import get_user_model


class ProfileView(DetailView):
    model = get_user_model()
    template_name = "users/profile.html"
    slug_field = "username"
