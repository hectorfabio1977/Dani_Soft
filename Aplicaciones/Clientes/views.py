from django.shortcuts import render
from Clientes.forms import ClienteForm


# Create your views here.
def Consulta_Clientes(request):
    form = ClienteForm()
    return render(request, 'Clientes.html',{'form': form})

