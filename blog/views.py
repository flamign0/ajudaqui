from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Anuncio
from .forms import AnuncioForm


def post_list(request):
    anuncios = Anuncio.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
    return render(request, 'blog/post_list.html', {'anuncios': anuncios})

def post_detail(request, pk):
    anuncio = get_object_or_404(Anuncio, pk=pk)
    return render(request, 'blog/post_detail.html', {'anuncio': anuncio})

@login_required
def post_new(request):
     if request.method == "POST":
         form = AnuncioForm(request.POST)
         if form.is_valid():
             anuncio = form.save(commit=False)
             anuncio.autor = request.user
             anuncio.data_publicacao = timezone.now()
             anuncio.save()
             return redirect('post_detail', pk=anuncio.pk)
     else:
         form = AnuncioForm()
     return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
     anuncio = get_object_or_404(Anuncio, pk=pk)
     if request.method == "POST":
         form = AnuncioForm(request.POST, instance=anuncio)
         if form.is_valid():
             anuncio = form.save(commit=False)
             anuncio.autor = request.user
             anuncio.data_publicacao = timezone.now()
             anuncio.save()
             return redirect('post_detail', pk=anuncio.pk)
     else:
         form = AnuncioForm(instance=anuncio)
     return render(request, 'blog/post_edit.html', {'form': form})
