from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Homepage do App de Filiação.</h1>")


def obterCliente(request, codCliente):
    return HttpResponse("<h2>Detalhes para o cliente id: " + str(codCliente) + "</h2>")
