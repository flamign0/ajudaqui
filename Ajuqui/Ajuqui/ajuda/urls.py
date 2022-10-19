from django.urls import path

from . import views

app_name = "ajuda"

urlpatterns = [
    path('', views.anuncioList, name='list'),
    path('anuncio/<int:pk>/', views.anuncioView, name='anuncio'),
    path('anuncioNew/', views.anuncioNew, name='anuncioNew'),
    path('edit/<int:pk>', views.editAnuncio, name='editAnuncio'),
    path('delete/<int:pk>', views.deleteAnuncio, name='deleteAnuncio'),
    
]