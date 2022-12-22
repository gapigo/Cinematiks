from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def catalogo_filmes(request):
    # return HttpResponse("""<html style="background: #000; color: #fff">Bem vindo ao catálogo de filmes</html>""")
    context = {'variavel': 'Matheus'}
    return render(request, 'catalogo.html', context)