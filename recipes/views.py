from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Recipe, RecipeIngredient

def detail(request, recipe_id):
    return HttpResponse("You're looking at recipe %s." % recipe_id)

def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})

def recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, 'recipe.html', {'recipe': recipe})

def edit(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    all_recipe_ingredients = RecipeIngredient.objects.all()
    if request.method == 'POST':
        recipe.name = request.POST.get('name')
        recipe.instructions = request.POST.get('instructions')
        
        # Get the list of recipeIngredient IDs from the form
        recipe_ingredient_ids = request.POST.getlist('recipe_ingredients')
        
        # Clear existing recipe ingredients and add the new ones
        recipe.ingredients.clear()
        for recipe_ingredient_id in recipe_ingredient_ids:
            recipe.ingredients.add(recipe_ingredient_id)
        
        recipe.save()
        return redirect('recipe', recipe_id=recipe_id)
    return render(request, 'edit.html', {'recipe': recipe, 'all_recipe_ingredients': all_recipe_ingredients})