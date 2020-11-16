from django.db import models
from django.utils import timezone

# カテゴリーモデル
class Category(models.Model):
    name = models.CharField('カテゴリー', max_length=50)

    def __str__(self):
        return self.name

class BaseModel(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, verbose_name = 'カテゴリー',
        on_delete = models.PROTECT
    )

    def __str__(self):
        return self.title