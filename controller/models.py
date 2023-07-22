from django.db import models

# Create your models here.

class Depoimentos(models.Model):
    depoimento = models.TextField(max_length=256)
    nome_da_pessoa = models.CharField(max_length=100)
    foto = models.CharField(max_length=50)