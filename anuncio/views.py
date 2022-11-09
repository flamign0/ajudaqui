from msilib.schema import ListView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from anuncio.models import Anuncio

class AnuncioList(ListView):
    model = Anuncio

class AnuncioDetail(DetailView):
    model = Anuncio

class AnuncioCreate(CreateView):
    model = Anuncio
    fields = '__all__'
    success_url: reverse_lazy('anuncio:anuncioList')

class AnuncioEdit(UpdateView):
    model = Anuncio
    fields = '__all__'
    success_url: reverse_lazy('anuncio:anuncioList')

class AnuncioDelete(DeleteView):
    queryset = Anuncio.objects.all()
    success_url = reverse_lazy('anuncio:anuncioList')

def anuncios_ativos(request):
    anuncios = Anuncio.objects.all().count()
    return render(request, 'anuncio_list.html', {'anuncios':anuncios})