from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Anuncio
from .forms import AnuncioForm

# Create your views here.


def anuncioList(request):
    anuncio = Anuncio.objects.all().order_by('-data_publicacao')
    return render(request, 'ajuda/list.html', {'anuncio': anuncio})


def anuncioView(request, pk):
    anuncio = get_object_or_404(Anuncio, pk=pk)
    return render(request, 'ajuda/anuncio.html', {'anuncio': anuncio})


def anuncioNew(request):
    if request.method == 'POST':
        form = AnuncioForm(request.POST)

        if form.is_valid():
            anuncio = form.save(commit=False)
            anuncio.autor = request.user
            anuncio.save()
            return redirect('/')

    else:
        form = AnuncioForm()
        return render(request, 'ajuda/anuncioNew.html', {'form': form})

def editAnuncio(request, pk):
    anuncio = get_object_or_404(Anuncio, pk=pk)
    form = AnuncioForm(instance=anuncio)

    if(request.method == 'POST'):
        form = AnuncioForm(request.POST, instance=anuncio)

        if(form.is_valid()):
            anuncio.save()
            return redirect('/')
        else:
            return render(request, 'ajuda/editAnuncio.html', {'form': form, 'anuncio': anuncio})

    else:
        return render(request, 'ajuda/editAnuncio.html', {'form': form, 'anuncio': anuncio})

def deleteAnuncio(request, pk):
    anuncio = get_object_or_404(Anuncio, pk=pk)
    anuncio.delete()
    return redirect('/')