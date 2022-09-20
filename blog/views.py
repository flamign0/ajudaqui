from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Anuncio


def post_list(request):
    anuncios = Anuncio.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
    return render(request, 'blog/post_list.html', {'anuncios': anuncios})

def post_detail(request, pk):
    anuncio = get_object_or_404(Anuncio, pk=pk)
    return render(request, 'blog/post_detail.html', {'anuncio': anuncio})