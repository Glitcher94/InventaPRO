from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Producto, Usuario



# Create your views here.

def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Realiza la validación del usuario
        try:
            user = Usuario.objects.get(correo=email, clave=password)
            if user.rol == 'Administrador':
                return HttpResponseRedirect('core/acceso_admin')
            elif user.rol == 'Trabajadora Social':
                return HttpResponseRedirect('core/vista_trab_social') 
            elif user.rol == 'DIDECO':
                return HttpResponseRedirect('core/vista_jefe_dideco')
            elif user.rol == 'Bodeguero':
                return HttpResponseRedirect('core/vista_enc_bodega')
            elif user.rol == 'Encargada inventario social':
                return HttpResponseRedirect('core/vista_enc_bodega')

        except Usuario.DoesNotExist:
            # Manejar el caso en que el usuario no exista o las credenciales sean incorrectas
            return render(request, 'index.html', {'error': 'Credenciales incorrectas'})

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
    context = {"inventario": data, "categorias": selec_categorias}

    if request.method == 'POST':
        print("Entré al bloque POST")  # Mensaje de depuración

        nombre_producto = request.POST['productName']
        categoria = request.POST['productCategory']
        cantidad = request.POST.get('productAmount', 0)
        unidad = request.POST['productUnitType']
        orden_compra = request.POST['productBuyOrder']

        # Mensaje de depuración
        print(f"Datos del formulario: {nombre_producto}, {categoria}, {cantidad}, {unidad}, {orden_compra}")

        producto = Producto(nombre_producto=nombre_producto, categoria=categoria, cantidad=cantidad, unidad=unidad,
                             orden_compra=orden_compra)
        
        if cantidad > 0:
            producto.estado = 'En stock'
        elif cantidad is None:
            producto.estado = 'Desconocido'
        else:
            producto.estado = 'Agotado'

        producto.save()

        messages.success(request, '¡Producto registrado con éxito!')

        print("Producto guardado en la base de datos")  # Mensaje de depuración

        return redirect('core/vista_enc_bodega')

    return render(request, 'core/vista_enc_bodega.html', context)


def vista_jefe_dideco(request):
    data = Producto.objects.all()  # Obtén todos los productos

    # Filtrar productos en función de la categoría y el estado
    categoria = request.GET.get('categoria')
    estado = request.GET.get('estado')

    if categoria:
        data = data.filter(categoria=categoria)

    if estado:
        data = data.filter(estado=estado)

    selec_categorias = Producto.objects.values_list('categoria', flat=True).distinct()
    context = {"inventario": data, "categorias": selec_categorias}

    if request.method == 'POST':
        print("Entré al bloque POST")  # Mensaje de depuración

        nombre_usuario = request.POST['userName']
        correo = request.POST['userEmail']
        clave = request.POST['userPin']
        rol = request.POST['userRol']

        # Mensaje de depuración
        print(f"Datos del formulario: {nombre_usuario}, {correo}, {clave}, {rol}")

        usuario = Usuario(nombre_usuario=nombre_usuario, correo=correo, clave=clave, rol=rol)

        usuario.save()

        messages.success(request, '¡Producto registrado con éxito!')

        print("Producto guardado en la base de datos")  # Mensaje de depuración

        return redirect('core/vista_jefe_dideco')

    return render(request, 'core/vista_jefe_dideco.html', context)




def vista_trab_social(request):
    data = Producto.objects.all()  # Obtén todos los productos

    # Filtrar productos en función de la categoría y el estado
    categoria = request.GET.get('categoria')
    estado = request.GET.get('estado')

    if categoria:
        data = data.filter(categoria=categoria)

    if estado:
        data = data.filter(estado=estado)

    selec_categorias = Producto.objects.values_list('categoria', flat=True).distinct()
    selec_productos = Producto.objects.values_list('nombre_producto', flat=True).distinct()
    context = {"inventario": data, "categorias": selec_categorias, "productos": selec_productos }

    return render(request, 'core/vista_trab_social.html', context)



def acceso_admin(request):
    return render(request, 'core/acceso_admin.html')