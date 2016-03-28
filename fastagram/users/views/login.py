from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse


class LoginView(View):

    def get(self, request):
        template_name = "users/login.html"

        return render(
            request,
            template_name,
            context={},
        )

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        next_page_url = request.POST.get("next") or reverse("home")

        user = authenticate(
            username=username,
            password=password,
        )

        if user:
            login(request, user)
            return redirect(next_page_url)
        return redirect(reverse("login"))
