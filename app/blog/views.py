from django.shortcuts import render
from django.views.generic import ListView
from .models import BaseModel

class BlogListView(ListView):
    template_name = 'top.html'
    model = BaseModel