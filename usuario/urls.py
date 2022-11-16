from .views import UsuarioCreate
from django.urls import path
from django.contrib.auth import views as auth_views



urlpatterns =[
    path('login/', auth_views.LoginView.as_view (template_name='usuario/login.html'), name='login'),
    path('usuario/', UsuarioCreate.as_view(), name='usuario'),
    path('logout/', auth_views.LogoutView.as_view (template_name='usuario/login.html'), name='logout'),
    
]