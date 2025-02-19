from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_login, name='index'),
    path('logout', views.user_logout, name='logout'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('mercado', views.mercado, name='mercado'),
    path('pet', views.pet, name='pet'),
    path('lazer', views.lazer, name='lazer'),
    path('viagem', views.viagem, name='viagem'),
    path('farmacia', views.farmacia, name='farmacia'),
    path('poupanca', views.poupanca, name='poupanca'),
    path('dashboards', views.dashboards, name='dashboards'),
    
]