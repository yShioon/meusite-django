from django.contrib import admin
from .models import Postagem, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug')
    prepopulated_fields = {'slug': ('nome',)}

@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'criado_em')
    list_filter = ('categoria', 'criado_em')
    search_fields = ('titulo', 'conteudo')
    prepopulated_fields = {'slug': ('titulo',)}
    fieldsets = (
        (None, {
            'fields': ('titulo', 'slug', 'resumo', 'conteudo')
        }),
        ('Informações Avançadas', {
            'fields': ('categoria', 'palavras_chave', 'imagem_destaque'),
            'classes': ('collapse',),
        }),
    )