from django.shortcuts import render, get_object_or_404
from .models import BaseModel, Category
import datetime


def CategoryFunc(request, category):
    category = Category.objects.get(name=category)
    blogCategory = BaseModel.objects.filter(category=category)
    return render(request, 'top.html', { 'category': category, 'blogCategory': blogCategory})

def BlogFunc(request):
    publish_list = BaseModel.objects.published()
    return render(request, 'top.html',  {'publish_list':publish_list})