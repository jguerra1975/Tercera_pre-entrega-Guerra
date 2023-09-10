from django.urls import path
from AppCoder.views import inicio, Pagina_Cliente , Crea_Cliente, Lista_Cliente, Busca_Cliente

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('cliente', Pagina_Cliente, name="Cliente"),
    path('crea-cliente', Crea_Cliente, name="CreaCliente"),
    path('dato_creado', Lista_Cliente, name="ListaCliente"),
    path('buscar-cliente', Busca_Cliente, name="BuscarCliente"),
#    path('crear-categorias', Crear_Categorias, name="CrearCategorias"),
#    path('buscar-categorias', Buscar_Categorias, name="BuscarCategorias"),
#    path('crear-articulos', Crear_Articulos, name="CrearArticulos"),
#    path('buscar-articulos', Buscar_Articulos, name="BuscarArticulos"),

]