from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Libro
from .form import LibroForm

# Create your views here.

def inicio(request):
    return render (request,'paginas/inicio.html') 
def nosotros(request):
    return render (request,'nosotros.html')    
def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html',{'formulario': formulario} )    
def editar(request,id):
    libro= Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario': formulario})
def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')

