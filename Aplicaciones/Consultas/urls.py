from django.urls import path
from .views import *


urlpatterns = [
    path("", departamento_view,name='Consultar departamentos'),
    

]