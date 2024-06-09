from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
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
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            items = form.save(commit=False)
            items.created_by = request.user
            items.save()

            return redirect('items:detail', pk=items.id)
    else:
        form = NewItemForm()
    form = NewItemForm()
    return render(request, 'items/form.html',{
        'form':form,
        'title': 'New Item',
    })