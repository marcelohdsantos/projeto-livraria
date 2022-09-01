from django.shortcuts import render, redirect
from .models import Livro
import requests


# Create your views here.


def home(request):
    livrosListados = Livro.objects.all()
    return render(request, 'gestaoLivros.html', {"livros": livrosListados})


def registrarLivro(request):
    codigo = request.POST['numCodigo']
    titulo = request.POST['txtTitulo']
    autor = request.POST['nomeAutor']

    livro = Livro.objects.create(codigo=codigo, titulo=titulo, autor=autor)
    return redirect('/')
