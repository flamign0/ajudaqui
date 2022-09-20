from django.db import models
from django.conf import settings
from django.utils import timezone


class Anuncio(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tipoSv = models.CharField(max_length=200)
    descSv = models.TextField()
    data_publicacao = models.DateTimeField(blank=True, null=True)
    email = models.EmailField()
    endereco = models.CharField(max_length=50)
    telefone = models.IntegerField()

    def publicar(self):
        self.data_publicacao = timezone.now()
        self.save()

    def __str__(self):
        return self.tipoSv
