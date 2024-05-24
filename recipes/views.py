from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

def detail(request, recipe_id):
    return HttpResponse("You're looking at recipe %s." % recipe_id)

def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})

def recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, 'recipe.html', {'recipe': recipe})