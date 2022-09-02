from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('registrarLivro/', views.registrarLivro),
    path('edicaoLivro/<codigo>', views.edicaoLivro),
    path('editarLivro/', views.editarLivro),
    path('excluirLivro/<codigo>', views.excluirLivro)
]