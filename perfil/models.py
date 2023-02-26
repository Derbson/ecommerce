from django.db import models
from .enderecos import estados
from django.contrib.auth.models import User


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    idade = models.PositiveIntegerField()
    data_nascimento = models.DateField()
    cpf = models.CharField(unique=True, max_length=11)
    enderecos = models.CharField(max_length=50)
    complemento = models.CharField(max_length=5)
    bairro = models.CharField(max_length=30)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(
        max_length=2,
        default='SP',
        choices=estados,
        )
    
    def __str__(self):
        return f'{self.usuario.first_name} {self.usuario.last_name}'

    class Meta:
        verbose_name_plural = 'Perfis'