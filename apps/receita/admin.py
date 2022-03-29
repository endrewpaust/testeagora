from django.contrib import admin
from .models import receita_modelo
class Listandoreceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria','tempo_de_preparo','publicada')
    # list links mostra quais displays serao clicados para
    # alterar a receita
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_per_page = 2
    list_editable = ('publicada',)

# registra o modelo no site
admin.site.register(receita_modelo,Listandoreceitas)