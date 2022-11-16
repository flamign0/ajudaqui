from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic import DetailView, ListView, TemplateView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from anuncio.models import Anuncio

from django.contrib.auth.mixins import LoginRequiredMixin

from braces.views import GroupRequiredMixin

class HomeView(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    group_required = [u"Admin", u"User"]
    template_name = 'anuncio/home.html'

class AnuncioList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Admin", u"User"]
    model = Anuncio

class AnuncioDetail(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    group_required = [u"Admin", u"User"]
    model = Anuncio

class AnuncioCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"Admin", u"User"]
    model = Anuncio
    fields = '__all__'
    success_url: reverse_lazy('anuncio:anuncioList')

class AnuncioEdit(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"Admin", u"User"]
    model = Anuncio
    fields = '__all__'
    success_url: reverse_lazy('anuncio:anuncioList')

class AnuncioDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u"Admin", u"User"]
    queryset = Anuncio.objects.all()
    success_url = reverse_lazy('anuncio:anuncioList')

    def anuncios_ativos(request):
        anuncios = Anuncio.objects.all().count()
        return render(request, 'anuncio_list.html', {'anuncios':anuncios})