from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.ctg_list, name='ctg_list'),
    path('form/', views.form, name='ctg_form'),
    path('detail/<int:pk>/', views.detail, name='ctg_detail'),
]
