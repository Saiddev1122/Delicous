from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug>/', views.index, name='index_s'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('element/', views.elements, name='element'),
    path('search/', views.search, name='search'),
    path('recipess/', views.search, name='recipess'),
    path('recipess/<int:pk>/', views.search, name='recipess'),
]
