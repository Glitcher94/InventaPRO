from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Producto

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def vista_enc_bodega(request):
    data = Producto.objects.all()  # Obtén todos los productos

    # Filtrar productos en función de la categoría y el estado
    categoria = request.GET.get('categoria')
    estado = request.GET.get('estado')

    if categoria:
        data = data.filter(categoria=categoria)

    if estado:
        data = data.filter(estado=estado)

    selec_categorias = Producto.objects.values_list('categoria', flat=True).distinct()
    context = {"productos": data, "categorias": selec_categorias}

    if request.method == 'POST':
        print("Entré al bloque POST")  # Mensaje de depuración

        nombre_producto = request.POST['productName']
        categoria = request.POST['productCategory']
        cantidad = request.POST.get('productAmount', 0)
        unidad = request.POST['productUnitType']

        print(f"Datos del formulario: {nombre_producto}, {categoria}, {cantidad}, {unidad}")  # Mensaje de depuración

        producto = Producto(nombre_producto=nombre_producto, categoria=categoria, cantidad=cantidad, unidad=unidad)
        producto.save()

        messages.success(request, '¡Producto registrado con éxito!')

        print("Producto guardado en la base de datos")  # Mensaje de depuración

        return redirect('core:vista_enc_bodega')

    return render(request, 'core/vista_enc_bodega.html', context)


def vista_jefe_dideco(request):
    data = Producto.objects.all()
    context = {"productos": data}
    return render(request, 'core/vista_jefe_dideco.html', context)