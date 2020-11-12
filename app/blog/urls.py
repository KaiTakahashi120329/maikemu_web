from django.urls import path
from .views import BlogFunc

urlpatterns = [
    path('', BlogFunc, name='list'),
]
