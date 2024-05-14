from django.urls import path

from .views import post_create

app_name = "blog"

urlpatterns = [
    path("create/", post_create, name="create"),
]
