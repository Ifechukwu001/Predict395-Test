from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path("", include("accounts.urls")),
    path("", RedirectView.as_view(url="blog/")),
    path("blog/", include("blog.urls")),
    path("admin/", admin.site.urls),
]
