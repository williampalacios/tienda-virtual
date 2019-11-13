from django.shortcuts import render

# Create your views here.
def prod_list(request):
    return render(request, 'catalogo/prod_list.html', {})
