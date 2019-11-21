from django.shortcuts import render
from .models import About

# Create your views here.

def about_page(request):
    model = About.objects.all()
    context = {'model':model}
    return render(request, 'about.html', context)
    
