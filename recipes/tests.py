from django.test import TestCase
from .models import Ingredient, RecipeIngredient, Recipe

class IngredientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Ingredient.objects.create(name='Test Ingredient')

    def test_name_label(self):
        ingredient = Ingredient.objects.get(id=1)
        field_label = ingredient._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        ingredient = Ingredient.objects.get(id=1)
        max_length = ingredient._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_str_representation(self):
        ingredient = Ingredient.objects.get(id=1)
        self.assertEqual(str(ingredient), ingredient.name)

class IngredientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Ingredient.objects.create(name='Test Ingredient')

    def test_name_label(self):
        ingredient = Ingredient.objects.get(id=1)
        field_label = ingredient._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        ingredient = Ingredient.objects.get(id=1)
        max_length = ingredient._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_str_representation(self):
        ingredient = Ingredient.objects.get(id=1)
        self.assertEqual(str(ingredient), ingredient.name)

class RecipeIngredientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ingredient = Ingredient.objects.create(name='Test Ingredient')
        RecipeIngredient.objects.create(ingredient=ingredient, quantity='2', unit='cups')

    def test_ingredient_label(self):
        recipe_ingredient = RecipeIngredient.objects.get(id=1)
        field_label = recipe_ingredient._meta.get_field('ingredient').verbose_name
        self.assertEqual(field_label, 'ingredient')

    def test_quantity_label(self):
        recipe_ingredient = RecipeIngredient.objects.get(id=1)
        field_label = recipe_ingredient._meta.get_field('quantity').verbose_name
        self.assertEqual(field_label, 'quantity')

    def test_unit_label(self):
        recipe_ingredient = RecipeIngredient.objects.get(id=1)
        field_label = recipe_ingredient._meta.get_field('unit').verbose_name
        self.assertEqual(field_label, 'unit')

    def test_str_representation(self):
        recipe_ingredient = RecipeIngredient.objects.get(id=1)
        expected_str = f'{recipe_ingredient.quantity} {recipe_ingredient.unit} de {recipe_ingredient.ingredient.name}'
        self.assertEqual(str(recipe_ingredient), expected_str)

class RecipeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        recipe = Recipe.objects.create(name='Test Recipe', instructions='Test instructions')
        ingredient = Ingredient.objects.create(name='Test Ingredient')
        recipe_ingredient = RecipeIngredient.objects.create(ingredient=ingredient, quantity='2', unit='cups')
        recipe.ingredients.add(recipe_ingredient)

    def test_name_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_instructions_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('instructions').verbose_name
        self.assertEqual(field_label, 'instructions')

    def test_ingredients_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('ingredients').verbose_name
        self.assertEqual(field_label, 'ingredients')

    def test_str_representation(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(str(recipe), recipe.name)