from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from fastagram.views import *
from users.views import *
from posts.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^signup/$', SignupView.as_view(), name='signup'),

    url(r'^posts/$', PostListView.as_view(), name='posts'),
    url(r'^posts/(?P<slug>\w+)/$', PostDetailView.as_view(), name='post'),
    url(r'^posts/(?P<slug>\w+)/comments/$', PostCommentCreateView.as_view(), name='post-comments'),

    url(r'^(?P<slug>\w+)/$', ProfileView.as_view(), name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
