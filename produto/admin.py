from django.contrib import admin
from .models import Produto, Variacao


class ProdutosAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "slug", "preco_marketing", "preco_promocional", "tipo")
    list_display_links = ("id", "nome")

admin.site.register(Produto, ProdutosAdmin)
admin.site.register(Variacao)
