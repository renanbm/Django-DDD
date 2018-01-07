from django.http import HttpResponse
from .models import Cliente, Endereco


def index(request):
    clientes = Cliente.objects.all()

    html = ''

    for cliente in clientes:
        url = '/filiacao/' + str(cliente.CodCliente) + '/'
        html += '<a href="' + url + '">' + cliente.Nome + '</a><br>'

    return HttpResponse(html)


def obterCliente(request, codCliente):
    return HttpResponse("<h2>Detalhes para o cliente id: " + str(codCliente) + "</h2>")
