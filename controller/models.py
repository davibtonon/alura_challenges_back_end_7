from django.db import models

# Create your models here.

class Depoimentos(models.Model):
    depoimento = models.TextField(max_length=256)
    nome_da_pessoa = models.CharField(max_length=100)
    foto = models.CharField(max_length=50)


class Destinos(models.Model):
    foto = models.CharField("Foto 1", max_length=50)
    foto_2 = models.CharField(max_length=50)
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    meta = models.CharField(max_length=160)
    texto_descritivo = models.CharField(max_length=200, default="")
