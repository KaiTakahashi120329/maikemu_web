from django.urls import path
from .views import BlogFunc, CategoryFunc, DetailFunc, ContactView, ContentView, SendEmailView, SuccessFunc
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', BlogFunc, name='list'),
    path('category/<str:category>', CategoryFunc, name='category'),
    path('detail/<int:pk>/', DetailFunc, name='detail'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/content/', ContentView.as_view(), name='content'),
    path('contact/send_email/', SendEmailView.as_view(), name='send'),
    path('contact/success/', SuccessFunc, name='success'),
]
