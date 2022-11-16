from . import views
from django.urls import path

app_name = 'anuncio'

urlpatterns =[
    path('', views.HomeView.as_view(), name='home'),
    path('lista/', views.AnuncioList.as_view(), name='anuncioList'),
    path('anuncio/<int:pk>/', views.AnuncioDetail.as_view(), name='anuncioDetail'),
    path('create/', views.AnuncioCreate.as_view(), name='anuncioCreate'),
    path('edit/<int:pk>/', views.AnuncioEdit.as_view(template_name="anuncio/anuncio_updated.html"), name='anuncioEdit'),
    path('delete/<int:pk>/', views.AnuncioDelete.as_view(), name='anuncioDelete'),
]