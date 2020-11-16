from django.contrib import admin
from .models import BaseModel, Category

admin.site.register(BaseModel)
admin.site.register(Category)