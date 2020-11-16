from django.shortcuts import render, get_object_or_404
from .models import BaseModel, Category


def CategoryFunc(request, category):
    category = Category.objects.get(name=category)
    blogCategory = BaseModel.objects.filter(category=category)
    return render(request, 'top.html', { 'category': category, 'blogCategory': blogCategory, 'test': test })

def BlogFunc(request):
    object_list = BaseModel.objects.all()
    return render(request, 'top.html',  {'object_list':object_list})