from django.urls import path
from .views import BlogFunc, CategoryFunc, DetailFunc

urlpatterns = [
    path('', BlogFunc, name='list'),
    path('category/<str:category>', CategoryFunc, name='category'),
    path('detail/<int:pk>/', DetailFunc, name='detail'),
]
