from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def vista_enc_bodega(request):
    data = Producto.objects.all()
    context = {"productos": data}
    return render(request, 'core/vista_enc_bodega.html', context)

def vista_jefe_dideco(request):
    data = Producto.objects.all()
    context = {"productos": data}
    return render(request, 'core/vista_jefe_dideco.html', context)
