from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='index'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('mercado', views.mercado, name='mercado'),
    path('pet', views.pet, name='pet'),
    path('dashboard', views.dashboard, name='dashboard'),
]