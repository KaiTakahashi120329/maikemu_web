from django.urls import path
from .views import BlogFunc, CategoryFunc

urlpatterns = [
    path('', BlogFunc, name='list'),
    path('category/<str:category>', CategoryFunc, name='category')
]
