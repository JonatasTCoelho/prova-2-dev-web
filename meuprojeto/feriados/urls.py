from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('cadastro', views.cadastro_feriados, name='cadastro'),
]