import uuid
from django.db import models


class FavoriteUrls(models.Model):
    class Meta:
        db_table = 'favorite_urls'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)

    def __str__(self):
        return self.title