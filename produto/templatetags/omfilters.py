from django.template import Library

register = Library()

@register.filter
def formata_preco(val):
    valor = ''
    inteiro, decimal = str(val).split('.')
    inteiro = [i for i in inteiro]

    for index, numero in enumerate(inteiro[::-1], 1):
        valor += numero
        if index % 3 == 0 and index != len(inteiro):
            valor += '.'

    return f'R$ {valor[::-1]},{decimal}'



