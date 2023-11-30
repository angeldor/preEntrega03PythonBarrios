from django.shortcuts import render
from .models import Blog, Category

# Create your views here.
def index(request):
    # Obtener todos los blogs
    blogs = Blog.objects.all()

    # Renderizar la plantilla
    return render(request, 'index.html', {'blogs': blogs})

def search(request):
    # Obtener la consulta de búsqueda
    consulta = request.GET.get('q')

    # Si no hay consulta, devolver una lista vacía
    if not consulta:
        blogs = []
    else:
        # Buscar los blogs que coincidan con la consulta
        blogs = Blog.objects.filter(titulo__icontains=consulta)

    # Renderizar la plantilla
    return render(request, 'index.html', {'blogs': blogs})

def categoria(request, categoria):
    # Obtener todos los blogs de la categoría especificada
    blogs = Blog.objects.filter(categoria__nombre=categoria)

    # Renderizar la plantilla
    return render(request, 'index.html', {'blogs': blogs})
