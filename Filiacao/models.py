from django.db import models
from datetime import datetime
import uuid


class Cliente(models.Model):
    CodCliente = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Nome = models.CharField(max_length=100)
    Cpf = models.CharField(max_length=11)
    Email = models.EmailField(max_length=100, blank=True)
    DataNascimento = models.DateField(default=datetime.min, blank=True)
    DataCadastro = models.DateTimeField(default=datetime.now, blank=True)
    Ativo = models.BooleanField(default=True)


class Endereco(models.Model):
    CodEndereco = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    CodCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Logradouro = models.CharField(max_length=250)
    Numero = models.CharField(max_length=10)
    Complemento = models.CharField(max_length=250)
    Bairro = models.CharField(max_length=100)
    Cep = models.CharField(max_length=8)
    Cidade = models.CharField(max_length=70)
    Estado = models.CharField(max_length=70)
    Ativo = models.BooleanField(default=True)
