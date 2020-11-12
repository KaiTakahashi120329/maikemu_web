from django.shortcuts import render, get_object_or_404
from .models import BaseModel


def BlogFunc(request):
    object_list = BaseModel.objects.all()
    return render(request, 'top.html',  {'object_list':object_list})