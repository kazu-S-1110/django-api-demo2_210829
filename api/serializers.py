from rest_framework import serializers

from .models import FavoriteUrls


class FavoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteUrls
        fields = ["id", "title", "url"]
