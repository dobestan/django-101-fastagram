from django.conf.urls import url
from django.contrib import admin

from users.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', LoginView.as_view(), name='login'),
]
