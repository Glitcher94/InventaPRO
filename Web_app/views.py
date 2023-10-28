from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def panel_inv_eb(request):
    data = Producto.objects.all()
    context = {"productos": data}
    return render(request, 'core/panel_inv_eb.html', context)
