from django.urls import path

from .views import post_create, post_list, post_detail, post_update

app_name = "blog"

urlpatterns = [
    path("create/", post_create, name="create"),
    path("", post_list, name="list"),
    path("<int:pk>/", post_detail, name="detail"),
    path("<int:pk>/update/", post_update, name="update"),
]
