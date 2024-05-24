from django.test import TestCase
from django.urls import reverse
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

class RecipeViewsTestCase(TestCase):
    def setUp(self):
        self.ingredient = Ingredient.objects.create(name="Test Ingredient")
        
        self.recipe = Recipe.objects.create(name="Test Recipe", instructions="Test Instructions")
        self.recipe_ingredient = RecipeIngredient.objects.create(
            ingredient=self.ingredient,
            quantity="1",
            unit="unit",
        )
        self.recipe.ingredients.add(self.recipe_ingredient)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Recipe")

    def test_recipe_view(self):
        response = self.client.get(reverse('recipe', args=(self.recipe.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Recipe")
        self.assertContains(response, "Test Instructions")
        self.assertContains(response, "Test Ingredient")

    def test_edit_view(self):
        new_name = "Updated Recipe Name"
        new_instructions = "Updated Instructions"
        new_ingredient_name = "Updated Ingredient"
        
        self.ingredient.name = new_ingredient_name
        self.ingredient.save()

        response = self.client.post(reverse('edit_recipe', args=(self.recipe.id,)), {
            'name': new_name,
            'instructions': new_instructions,
            'recipe_ingredients': [self.recipe_ingredient.id],
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful POST
        updated_recipe = Recipe.objects.get(pk=self.recipe.id)
        self.assertEqual(updated_recipe.name, new_name)
        self.assertEqual(updated_recipe.instructions, new_instructions)
        self.assertEqual(updated_recipe.ingredients.count(), 1)
        self.assertEqual(updated_recipe.ingredients.first().ingredient.name, new_ingredient_name)


    def test_detail_view(self):
        response = self.client.get(reverse('recipe', args=(self.recipe.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Recipe")