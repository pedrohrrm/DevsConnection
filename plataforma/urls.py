from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('projetos/', views.projetos, name='projetos'),
    path('sobre/', views.sobre, name='sobre'),
    path('orcamento/', views.orcamento, name='orcamento'),
]