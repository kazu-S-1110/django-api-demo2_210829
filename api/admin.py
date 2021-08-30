from django.contrib import admin
from .models import FavoriteUrl


class FavoModelAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "id", "created_at")
    ordering = ("-created_at",)


admin.site.register(FavoriteUrl, FavoModelAdmin)
