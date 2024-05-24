from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:recipe_id>/', views.recipe, name='recipe'),
    path('<int:recipe_id>/edit/', views.edit, name='edit_recipe'),
]