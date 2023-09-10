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
            return render(req, "dato_creado.html", {"dato": 'Cliente'})
    else:
        miFormulario = FormularioClientes()
        return render(req, "FormularioClientes.html", {"miFormulario": miFormulario})
        
def Lista_Cliente(req):
    return render(req, "dato_creado.html")

def Busca_Cliente(req: HttpRequest):
    print('method', req.method)
    print('GET', req.GET)
    if req.GET["nombre"]:
        dato = req.GET["nombre"]
        #cliente = Clientes.objects.get(nombre=dato)
        #cliente = Clientes.objects.filter(nombre=dato)
        clientes = Clientes.objects.filter(nombre__icontains=dato)
        print (f'{clientes}')
        if clientes.exists():
            print ('paso el nombre')
        else:
            clientes = Clientes.objects.filter(apellidoPaterno__icontains=dato)
            print ('paso el Apellido Paterno')
            if clientes.exists():
                print ('paso el Apellido Materno')
            else:
                clientes = Clientes.objects.filter(apellidoMaterno__icontains=dato)
                if clientes.exists():
                    pass
                else:
                    clientes = Clientes.objects.filter(dni__icontains=dato)
                    if clientes.exists():
                        pass
                    else:
                        return render(req, "no_existe_dato.html", {"dato": 'Cliente'})

        return render(req, "BusquedaCliente.html", {"clientes": clientes})
    else:
        return render(req, "no_existe_dato.html", {"dato": 'Cliente'})