from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Items
from .forms import NewItemForm

def detail(request, pk):
    items = get_object_or_404(Items, pk=pk)
    related_items = Items.objects.filter(category=items.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'items/detail.html', {
        'items':items,
        'related_items':related_items,
    })

@login_required
def new(request):
    form = NewItemForm()
    return render(request, 'items/form.html',{
        'form':form,
        'title': 'New Item',
    })