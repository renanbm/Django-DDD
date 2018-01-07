from django.conf.urls import url
from . import views

urlpatterns = [
    # /filiacao/
    url(r'^$', views.index, name='index'),

    # /filiacao/14f95d5a-6832-4c4b-81c6-e6120038326c/
    url(r'^(?P<codCliente>[{(]?[0-9a-fA-F]{8}[-]?([0-9a-fA-F]{4}[-]?){3}[0-9a-fA-F]{12}[)}]?)/$', views.obterCliente, name='obterCliente'),
]
