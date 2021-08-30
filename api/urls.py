from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register("Favo", views.FavoViewset)

app_name = "FavoriteUrls"

urlpatterns = [
    path("", include(router.urls))
]
