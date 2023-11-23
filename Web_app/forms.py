from django import forms
from .models import Producto  # Importa tu modelo Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'categoria', 'cantidad', 'unidad', 'orden_compra']

    # Puedes agregar validaciones adicionales si es necesario
    def clean(self):
        cleaned_data = super().clean()
        # Agrega validaciones personalizadas si las necesitas
        return cleaned_data