from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Homepage do App de Filiação.</h1>")