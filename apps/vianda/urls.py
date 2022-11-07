from django.urls import path

from apps.usuario import views
from apps.vianda.views import listar_vianda, registrar_vianda

app_name = 'vianda'
urlpatterns = [
    path('add-vianda', registrar_vianda, name='registrar_vianda'),
    path('list-vianda/<int:pk>', listar_vianda, name='listar_vianda')
]