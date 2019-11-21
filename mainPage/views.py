from django.shortcuts import render
from .models import MainPage, About

# Create your views here.
def home(request):
    main_page_source = MainPage.objects.all()
    about = About.objects.all()
    context = {'main_page_source': main_page_source,
               'about': about,}
    return render(request, 'base.html', context)


def about(request):
    about = About.objects.all()
    context = {'about': about,}
    return render(request, 'about.html', context)
