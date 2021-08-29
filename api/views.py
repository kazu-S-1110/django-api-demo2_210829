from rest_framework import viewsets
from django.shortcuts import render

from .models import FavoriteUrls
from .serializers import FavoSerializer


class FavoViewset(viewsets.ModelViewSet):
    queryset = FavoriteUrls.objects.all()
    serializer_class = FavoSerializer
