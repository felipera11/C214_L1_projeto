from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

# Create your views here.

def detail(request, recipe_id):
    return HttpResponse("You're looking at recipe %s." % recipe_id)

def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})

