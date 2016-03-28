from django.contrib.auth import login
from django.views.generic import View
from django.shortcuts import render


class LoginView(View):

    def get(self, request):
        template_name = "users/login.html"

        return render(
            request,
            template_name,
            context={},
        )

    def post(self, request):
        pass
