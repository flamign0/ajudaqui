from django.shortcuts import render
from django.utils import timezone
from .models import Anuncio


def post_list(request):
    anuncios = Anuncio.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
    return render(request, 'blog/post_list.html', {'anuncios': anuncios})