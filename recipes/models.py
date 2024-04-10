from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)
    unit = models.CharField(max_length=20)  # New field for unit of measurement
   
    def __str__(self):
        return f'{self.quantity} {self.unit} of {self.ingredient.name}'

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(RecipeIngredient)
    instructions = models.TextField()

    def __str__(self):
        return self.name


