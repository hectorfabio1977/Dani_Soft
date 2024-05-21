from django.urls import path
from . import views


urlpatterns = [
    path("",views.Consulta_Clientes, name='Clientes_consultas'),
]
