from django.shortcuts import render
from items.models import Category, Items

from .forms import SignupForm

# Create your views here.
def index(request):
    items = Items.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html',{
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    form = SignupForm()

    return render(request, 'core/signup.html', {
        'form':form,
    })


