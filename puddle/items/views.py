from django.shortcuts import render, get_object_or_404
from .models import Items

def detail(request, pk):
    items = get_object_or_404(items, pk=pk)

    return render(request, 'items/detail.html', {
        'items':items,
    })