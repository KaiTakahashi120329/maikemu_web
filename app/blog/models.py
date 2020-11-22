from django.db import models
from django.utils import timezone


# カテゴリーモデル
class Category(models.Model):
    name = models.CharField('カテゴリー', max_length=50)

    def __str__(self):
        return self.name

# 予約投稿機能のためマネージャーの作成
class DiaryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish_at__lte=timezone.now())

# 投稿機能のモデル
class BaseModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=25, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, verbose_name = 'カテゴリー',
        on_delete = models.PROTECT
    )
    publish_at = models.DateTimeField('作成日', default=timezone.now)
    objects = DiaryQuerySet.as_manager()

    def __str__(self):
        return self.title