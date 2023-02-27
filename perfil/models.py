from django.db import models
from .enderecos import estados
from django.contrib.auth.models import User
from django.forms import ValidationError
from . import validators


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
        return f'{self.usuario}'

    def clean(self):
        error_messages = {}
        
        if not validators.validate_cpf(self.cpf):
            error_messages['cpf'] = 'Erro: Digite um cpf válido.'
        
        if not validators.validate_age(self.idade):
            error_messages['idade'] = 'Error: Corrija idade'

        if not validators.validate_cep(self.cep):
            error_messages['cep'] = 'CEP inválido, digite apenas números'

        if not validators.valida_data_nascimento(self.idade, self.data_nascimento):
            error_messages['data_nascimento'] = 'Data não condiz com a idade.'
        
        if error_messages:
            raise ValidationError(error_messages)
       
        
    class Meta:
        verbose_name_plural = 'Perfis'