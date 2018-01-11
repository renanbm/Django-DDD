from django.http import Http404
from django.shortcuts import render
from .models import Cliente, Endereco


def index(request):
    clientes = Cliente.objects.all()
    return render(request, 'Filiacao/index.html', {'clientes': clientes})


def obterCliente(request, codCliente):
    try:
        cliente = Cliente.objects.get(pk=codCliente)
    except Cliente.DoesNotExist:
        raise Http404("O cliente solicitado não existe na base de dados.")
    return render(request, 'Filiacao/detalhes.html', {'cliente' : cliente})
