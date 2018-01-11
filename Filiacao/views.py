from django.http import HttpResponse
from django.template import loader
from .models import Cliente, Endereco


def index(request):
    clientes = Cliente.objects.all()
    template = loader.get_template('Filiacao/index.html')
    context = {
        'clientes': clientes,
    }
    return HttpResponse(template.render(context, request))


def obterCliente(request, codCliente):
    return HttpResponse("<h2>Detalhes para o cliente id: " + str(codCliente) + "</h2>")
