from django.contrib.auth import login, authenticate, get_user_model
from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse


class SignupView(View):

    def get(self, request):
        template_name = "users/signup.html"

        return render(
            request,
            template_name,
            context={},
        )

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = get_user_model().objects.create_user(
            username=username,
            password=password,
        )

        # Automatically login user after signup
        user = authenticate(
            username=username,
            password=password,
        )
        login(request, user)

        return redirect(reverse("home"))
