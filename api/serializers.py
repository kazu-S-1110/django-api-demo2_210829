from rest_framework import serializers

from .models import FavoriteUrl


class FavoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteUrl
        fields = ["id", "title", "url", "created_at"]
