from django.contrib import admin
from .models import FavoriteUrls

class FavoModelAdmin(admin.ModelAdmin):
    list_display = ("title","url" "id", "created_at")
    ordering = ("-created_at",)


admin.site.register(FavoriteUrls, FavoModelAdmin)