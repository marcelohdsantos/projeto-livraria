from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('registrarLivro/', views.registrarLivro),
]