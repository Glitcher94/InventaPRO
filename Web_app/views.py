from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def panel_inv_eb(request):
    return render(request, 'panel_inv_eb.html')