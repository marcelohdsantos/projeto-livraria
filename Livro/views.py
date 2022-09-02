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


def edicaoLivro(request, codigo):
    livro = Livro.objects.get(codigo=codigo)
    return render(request, 'edicaoLivro.html', {"livro": livro})


def editarLivro(request):
    codigo = request.POST['numCodigo']
    titulo = request.POST['txtTitulo']
    autor = request.POST['nomeAutor']

    livro = Livro.objects.get(codigo=codigo)
    livro.titulo = titulo
    livro.autor = autor
    livro.save()

    return redirect('/')


def excluirLivro(request, codigo):
    livro = Livro.objects.get(codigo=codigo)
    livro.delete()

    return redirect('/')
