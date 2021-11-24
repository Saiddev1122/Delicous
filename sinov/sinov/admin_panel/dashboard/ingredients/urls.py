from django.urls import path
from dashboard.ingredients import views

urlpatterns = [
    path('list/', views.ingedient_list, name='ingedient_list'),
    path('add/', views.ingedient_form, name='ingedient_form'),
    path('edit/<int:pk>/', views.ingedient_form, name='ingedient_form_edit'),
    path('delete/<int:pk>/', views.delete_ingedient, name='delete'),
    path('detail/<int:pk>/', views.ingedient_detail, name='ingedient_detail')
]