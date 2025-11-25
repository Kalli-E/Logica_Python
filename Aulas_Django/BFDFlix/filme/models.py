from django.db import models
from django.utils import timezone

# Create your models here.

LISTA_CATEGORIAS = (
    ("AULAS", "Aulas"),
    ("PROGRAMACAO", "Programação"),
    ("CURSOS", "Cursos"),
    ("PROVAS", "Provas"),
    ("CICLOS", "Ciclos"),
    ("OUTROS", "Outros"),
)

#Criar o filme
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.CharField(max_length=1000)
    categoria = models.CharField(max_length=20, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    lancamento = models.DateTimeField(default=timezone.now)
    # data_cricao = models.DateTimeField(default=timezone.now)
     
    def __str__ (self):
        return self.titulo