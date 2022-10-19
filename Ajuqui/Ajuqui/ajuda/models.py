from operator import truediv
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Anuncio(models.Model):
    autor = models.ForeignKey(User,  on_delete=models.CASCADE)
    tipoSv = models.CharField(max_length=200)
    descSv = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    endereco = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.tipoSv

    
