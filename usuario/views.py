from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import UserForm

# Create your views here.


class UsuarioCreate(CreateView):
    template_name = "usuario/usuario.html"
    form_class = UserForm
    success_url = reverse_lazy('anuncio:home')

    def form_valid(self, form):

        grupo = get_object_or_404(Group, name='User')

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        return url




