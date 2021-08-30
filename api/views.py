from rest_framework import viewsets
from django.shortcuts import render

from .models import FavoriteUrl
from .serializers import FavoSerializer


class FavoViewset(viewsets.ModelViewSet):
    queryset = FavoriteUrl.objects.all()
    serializer_class = FavoSerializer
