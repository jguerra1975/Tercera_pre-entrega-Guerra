from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Articulos, Categorias, Clientes
from .forms import FormularioClientes, FormularioCategorias, FormularioArticulos

# Create your views here.

def inicio(req):
    return render(req, "inicio.html")

def Pagina_Cliente(req):
    return render(req, "clientes.html")

def Crea_Cliente(req):
    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':
        miFormulario = FormularioClientes(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            cliente = Clientes(dni=data["dni"], nombre=data["nombre"], apellidoPaterno=data["apellidoPaterno"], apellidoMaterno=data["apellidoMaterno"], email=data["email"])
            cliente.save()
            return render(req, "ListaClientes.html")
    else:
        miFormulario = FormularioClientes()
        return render(req, "FormularioClientes.html", {"miFormulario": miFormulario})
        
def Lista_Cliente(req):
    return render(req, "ListaClientes.html")

def Busca_Cliente(req: HttpRequest):
    print('method', req.method)
    print('GET', req.GET)
    if req.GET["nombre"]:
        dato = req.GET["nombre"]
        #cliente = Clientes.objects.get(nombre=nombre)
        #cliente = Clientes.objects.filter(nombre=nombre)
        clientes = Clientes.objects.filter(nombre__icontains=dato)
        print (f'{clientes}')
        for cliente in clientes:
            print(f'{cliente}')
 #       if clientes[nombre] == False:
 #           clientes = Clientes.objects.filter(apellidoPaterno__icontains=dato)
  #          print (f'{clientes}')
  #          if clientes[apellidoPaterno] == False:
  #              clientes = Clientes.objects.filter(apellidoMaterno__icontains=dato)
  #              print (f'{clientes}')

        return render(req, "BusquedaCliente.html", {"clientes": clientes})
    else:
        return HttpResponse(f'no hay resultados en la busqueda {req.GET["nombre"]}')