from django.views.generic import View
from django.shortcuts import render


class SignupView(View):

    def get(self, request):
        template_name = "users/signup.html"

        return render(
            request,
            template_name,
            context={},
        )

    def post(self, request):
        pass
