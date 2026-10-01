from django.shortcuts import render
from .models import categoria
from django.shortcuts import render, redirect

def crear(request):
    if request.method == 'POST':
        cat = categoria(
            nombre = request.POST["nombre"],
            observaciones = request.POST["observaciones"]
        )
        cat.save()
        return redirect('/categoria/lista/')
    return render(request, "formulario_categoria.html")

def listar(request):
    categorias = categoria.objects.all()
    return render(
        request,
        "lista_categoria.html",
        {"categorias": categorias}
    )

def detalle(request, id):
    cat = categoria.objects.get(id=id)
    return render(
        request, 
        "detalle_categoria.html", 
        {"categoria": cat}
    )

def editar(request, id):
    cat = categoria.objects.get(id=id)
    if request.method == "POST":
        cat.nombre = request.POST["nombre"]
        cat.observaciones = request.POST["observaciones"]
        cat.save()
        return redirect('/categoria/lista/')
    return render(
        request, 
        "formulario_categoria.html", 
        {"categoria": cat}
    )

def eliminar(request, id):
    cat = categoria.objects.get(id=id)
    cat.delete()
    return redirect('/categoria/lista/')