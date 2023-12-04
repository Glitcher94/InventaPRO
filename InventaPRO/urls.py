"""
URL configuration for InventaPRO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Web_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="core/index"),
    path('core/vista_enc_bodega', views.vista_enc_bodega, name="core/vista_enc_bodega"),
    path('core/vista_jefe_dideco', views.vista_jefe_dideco, name="core/vista_jefe_dideco"),
    path('core/vista_trab_social', views.vista_trab_social, name="core/vista_trab_social"),
    path('core/acceso_admin', views.acceso_admin, name="core/acceso_admin"),
    path('core/update_quantity/<int:product_id>/<int:new_quantity>/', views.update_quantity, name="core/update_quantity"),
    path('core/update_name/<int:product_id>/<str:new_name>/', views.update_name, name="core/update_name")
]