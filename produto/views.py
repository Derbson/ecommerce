from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from .models import Produto

class ListaProdutos(ListView):
    model = Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 10


class DetalheProdutos(DetailView):
    model = Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produtos'


# class DetalheProdutos(View):
#     pass

# class AdicinarAoCarrinho(View):
#     pass

# class RemoverDoCarrinho(View):
#     pass

# class Carrinho(View):
#     pass

# class Finalizar(View):
#     pass
