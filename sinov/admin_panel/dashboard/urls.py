from django.urls import path, include

urlpatterns = [
    path('ctg/', include('dashboard.category.urls')),
    path('recipe/', include('dashboard.recipes.urls')),
    path('ingredients/', include('dashboard.ingredients.urls')),
]