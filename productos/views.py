from django.shortcuts import redirect, render
from .forms import ProductoForm
from .models import Producto


def lista_productos(request):
    productos = Producto.objects.all().order_by('id')
    return render(request, 'lista.html', {'productos': productos})


def nuevo_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'formulario.html', {'form': form})
