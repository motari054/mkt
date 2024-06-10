from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Items, Category
from .forms import NewItemForm, EditItemForm

def item(request):
    query = request.GET.get('query', '')
    categories = Category.objects.all()
    item = Items.objects.filter(is_sold=False)

    if query:
        item = item.filter(Q(name__icontains=query)| Q(description__icontains=query))
    return render(request, 'items/item.html', {
        'item': item,
        'query': query,
        'categories':categories,
    })

def detail(request, pk):
    items = get_object_or_404(Items, pk=pk)
    related_items = Items.objects.filter(category=items.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'items/detail.html', {
        'items':items,
        'related_items':related_items,
    })

@login_required
def edit(request, pk):
    items = get_object_or_404(Items, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=items)
        if form.is_valid():
            form.save()

            return redirect('items:detail', pk=items.id)
    else:
        form = EditItemForm(instance=items)
    
    return render(request, 'items/form.html',{
        'form':form,
        'title': 'Edit Item',
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
    
    return render(request, 'items/form.html',{
        'form':form,
        'title': 'New Item',
    })

@login_required
def delete(request, pk):
    items = get_object_or_404(Items, pk=pk, created_by=request.user)
    items.delete()

    return redirect('dashboard/index.html')