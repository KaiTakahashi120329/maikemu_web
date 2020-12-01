from django.shortcuts import render, get_object_or_404
from .models import BaseModel, Category
import datetime


def CategoryFunc(request, category):
    category = Category.objects.get(name=category)
    publish_list = BaseModel.objects.published().filter(category=category)
    return render(request, 'category.html', { 'category':category, 'publish_list':publish_list})

def BlogFunc(request):
    publish_list = BaseModel.objects.published()
    return render(request, 'top.html',  {'publish_list':publish_list})

def DetailFunc(request, pk):
    object = get_object_or_404(BaseModel, pk=pk)
    return render(request, 'detail.html', {'object':object})