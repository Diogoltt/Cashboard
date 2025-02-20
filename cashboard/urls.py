from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_login, name='index'),
    path('logout', views.user_logout, name='logout'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('dashboards', views.dashboards, name='dashboards'),
    path('financas', views.financas, name='financas'),
    path("categoria/<str:categoria>/", views.categoria_view, name="categoria_view"),
    path('add_financa/', views.add_financa, name='add_financa'),
]