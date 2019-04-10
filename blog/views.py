from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Post
from django.urls import reverse
from .forms import HomeForm


def home(request):

    if request.method == 'POST':
     #   form = HomeForm(request.POST)
        form = HomeForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/home.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = HomeForm()

    return render(request, 'blog/home.html', {'form': form})



        
    
