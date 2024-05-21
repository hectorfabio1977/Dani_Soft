from django.shortcuts import render
from Consultas.forms import DepartamentoForm


# Create your views here.
def departamento_view(request):
    
    form = DepartamentoForm()
    #print(form)
    return render(request, 'Departamento.html',{'form':form})

"""def departamento_view(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            # Puedes agregar aquí redireccionamiento o cualquier otra lógica después de guardar el formulario
    else:
        form = DepartamentoForm()
    return render(request, 'Departamento.html', {'form': form})"""


