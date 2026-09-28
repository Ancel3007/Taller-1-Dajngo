from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'precio', 'cantidad']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del producto'}),
            'categoria': forms.TextInput(attrs={'placeholder': 'Categoría'}),
            'precio': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'cantidad': forms.NumberInput(attrs={'min': '0'}),
        }

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio < 0:
            raise forms.ValidationError('El precio no puede ser negativo.')
        return precio

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 0:
            raise forms.ValidationError('La cantidad no puede ser negativa.')
        return cantidad
