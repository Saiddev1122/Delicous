from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.recipe_list, name='recipe_list'),
    path('add/', views.recipe_form, name='recipe_form'),
    path('edit/<int:pk>/', views.recipe_form, name='recipe_form_edit'),
    path('delete/<int:pk>/', views.delete_recipe, name='delete'),
    path('detail/<int:pk>/', views.recipe_detail, name='recipe_detail')
]