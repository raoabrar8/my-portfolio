from django.shortcuts import render, redirect
from .forms import *
from .models import *
# Create your views here.


def home(request):
    
    home = Home.objects.latest('updated')
    
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)
    
    categories = Category.objects.all()
    
    portfolios = Portfolio.objects.all()
    context = {
        'home':home,
        'about':about,
        'profiles':profiles,
        'categories':categories,
        'portfolios':portfolios,
    }
    return render(request, 'portfolio/index.html', context)
