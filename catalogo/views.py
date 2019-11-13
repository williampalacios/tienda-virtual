from django.shortcuts import render
from .models import Producto

# Create your views here.
def prod_list(request):
    productos = Producto.objects.order_by('nombre')
    return render(request, 'catalogo/prod_list.html', {'prods': productos})
