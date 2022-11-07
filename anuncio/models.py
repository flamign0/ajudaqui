from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Anuncio(models.Model):
    autor = models.ForeignKey(User,  on_delete=models.CASCADE)
    tipoSv = models.CharField(max_length=200, verbose_name='Tipo de Serviço:')
    descSv = models.TextField(verbose_name='Descrição:')
    data_publicacao = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(verbose_name='Email:')
    endereco = models.CharField(max_length=50, verbose_name='Endereço:')
    telefone = models.CharField(max_length=20, verbose_name='Telefone:')

    def __str__(self):
        return self.tipoSv

    def get_absolute_url(self):
        return reverse('anuncio:anuncioDetail', args=[str(self.id)])