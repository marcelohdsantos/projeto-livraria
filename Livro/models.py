from django.db import models
from django.db.models import Model


# Create your models here.

class Livro(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.codigo)
