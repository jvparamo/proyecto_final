from django.urls import path, include
from .views import *

urlpatterns = [
    #path('usuario/', usuario, name = 'usuario'),
    path('registro/', registro, name='registro'),
    path('', gmail, name='gmail'),
    path('home', home, name='home'),
    path('editor', editor, name='editor'),
    path('estadistica', estadistica, name='estadistica'),
    path('perfil', perfil, name='perfil'),

]