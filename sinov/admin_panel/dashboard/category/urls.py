from django.urls import path
from dashboard.category import views

urlpatterns = [
    path('list/', views.ctg_list, name='ctg_list'),
    path('add/', views.ctg_form, name='ctg_form'),
    path('edit/<int:pk>/', views.ctg_form, name='ctgt_form_edit'),
    path('delete/<int:pk>/', views.delete_ctg, name='delete'),
    path('detail/<int:pk>/', views.ctg_detail, name='ctg_detail')
]