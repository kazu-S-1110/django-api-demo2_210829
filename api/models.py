import uuid
from django.db import models


class FavoriteUrl(models.Model):
    class Meta:
        verbose_name_plural = "お気に入りリスト"  # 管理画面のモデル名にSが付くのを防ぐ。
        db_table = 'favorite_url'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=30)
    url = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)

    def __str__(self):
        return self.title
