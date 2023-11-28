from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Producto, Usuario, Solicitud, MovimientosInventario
from django.db import transaction
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model





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

@transaction.atomic
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

    if request.method == 'POST':
        try:
            with transaction.atomic():
                nombre_producto = request.POST.get('productName')
                categoria = request.POST.get('productCategory')
                cantidad = request.POST.get('productAmount')
                unidad = request.POST.get('productUnitType')
                orden_compra = request.POST.get('productBuyOrder')

                print(f"Datos del formulario: {nombre_producto}, {categoria}, {cantidad}, {unidad}, {orden_compra}")

                cantidad_entero = int(cantidad) if cantidad else 0

                estado_producto = 'Desconocido'
                if cantidad_entero > 0:
                    estado_producto = 'En stock'
                elif cantidad_entero == 0:
                    estado_producto = 'Agotado'

                producto = Producto(
                    nombre_producto=nombre_producto,
                    categoria=categoria,
                    cantidad=cantidad_entero,
                    unidad=unidad,
                    orden_compra=orden_compra,
                    estado=estado_producto
                )
                producto.save()

                messages.success(request, '¡Producto registrado con éxito!')

                return redirect('core/vista_enc_bodega')

        except Exception as e:
            print(f"Error al guardar el producto: {e}")
            messages.error(request, 'Error al guardar el producto. Consulta los registros para más detalles.')
            return redirect('core/vista_enc_bodega')
    
    context = {"inventario": data, "categorias": selec_categorias}

    return render(request, 'core/vista_enc_bodega.html', context)

def update_quantity(request, product_id, new_quantity):
    producto = Producto.objects.get(id_producto=product_id)
    producto.cantidad = new_quantity
    producto.save()
    return JsonResponse({'new_quantity': producto.cantidad})

def update_name(request, product_id, new_name):
    producto = Producto.objects.get(id_producto=product_id)
    producto.nombre_producto = new_name
    producto.save()
    return JsonResponse({'new_name': producto.nombre_producto})





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

    usuarios = Usuario.objects.all()  # Obtener todos los usuarios

    context = {"inventario": data, "categorias": selec_categorias, 'usuarios': usuarios}

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

    if request.method == 'POST':
        fecha = request.POST['fecha']
        orden_compra = request.POST['ordenCompra']
        programa = request.POST['programa']
        tipo_solicitud = request.POST['tipo_solicitud']
        producto = request.POST['productName']
        cantidad = request.POST['cantidad']

        User = get_user_model()

        nueva_solicitud = Solicitud(
            fecha_solicitud=fecha,
            tipo_solicitud=tipo_solicitud,
            estado_solicitud='Pendiente', 
            beneficiario='Nombre del beneficiario', 
            programa=programa
        )
        nueva_solicitud.save()

        def generar_id_movimiento():
            fecha_actual = datetime.now()
            t_stamp = int(fecha_actual.timestamp()) * 1000
            # Utiliza un contador autoincrementable para los últimos 3 dígitos
            if not hasattr(generar_id_movimiento, "contador"):
                generar_id_movimiento.contador = 0
            generar_id_movimiento.contador += 1
            id_movimiento = f"{t_stamp}{generar_id_movimiento.contador:03d}"  # Asegura 3 dígitos
        
            return id_movimiento

        if producto:
            # Buscar el objeto Producto por su nombre
            producto_obj = get_object_or_404(Producto, nombre_producto=producto)
            id_movimiento = generar_id_movimiento()
            usuario_aut = User.objects.get(pk=request.user.pk)

            nuevo_movimiento = MovimientosInventario(
                id_movimiento=id_movimiento,
                id_producto=producto_obj,
                cantidad=cantidad,
                tipo_movimiento='egreso',  # Tipo de movimiento 'egreso'
                id_usuario=usuario_aut,  # Si tienes el usuario actual
                id_solicitud=nueva_solicitud,
                fecha_movimiento=datetime.now()  # Fecha actual
            )
            nuevo_movimiento.save()

        messages.success(request, '¡Solicitud enviada con éxito!')

        return redirect('core/vista_trab_social')


    return render(request, 'core/vista_trab_social.html', context)



def acceso_admin(request):
    return render(request, 'core/acceso_admin.html')