from validate_docbr import CPF
import re


def valida_cpf(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)


def valida_idade(idade):
    if idade <= 0 or idade >= 120:
        return False
    return True

def valida_cep(cep):
    if re.search(r'[^0-9]', cep) or len(cep) != 8:
        return False
    return True
    