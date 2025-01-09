from django.contrib import admin
from .models import Reclamacao, Assinatura, AssinaturaCliente, Servico, CategoriaLimite


class AssinaturaAdmin(admin.ModelAdmin):
    # Campos exibidos na lista de registros
    list_display = ('nome', 'tipo', 'preco', 'ordem', 'ativo', 'data_criacao', 'ultima_atualizacao')
    list_filter = ('tipo', 'ativo')  # Filtros laterais
    search_fields = ('nome', 'descricao1', 'descricao2', 'descricao3')  # Campos pesquisáveis
    ordering = ('ordem',)  # Ordenação padrão por ordem

    # Configuração para o formulário detalhado
    fieldsets = (
        ('Informações Gerais', {
            'fields': ('tipo', 'nome', 'preco', 'ordem', 'ativo'),
        }),
        ('Descrição e Links Associados', {
            'fields': (
                ('descricao1', 'link1'),
                ('descricao2', 'link2'),
                ('descricao3', 'link3'),
                ('descricao4', 'link4'),
                ('descricao5', 'link5'),
                ('descricao6', 'link6'),
                ('descricao7', 'link7'),
                ('descricao8', 'link8'),
                ('descricao9', 'link9'),
                ('descricao10', 'link10'),
            ),
            'description': 'Adicione as descrições e selecione os links associados.'
        }),
        ('Histórico', {
            'fields': ('data_criacao', 'ultima_atualizacao'),
            'description': 'Informações sobre a criação e última atualização do registro.',
        }),
    )
    readonly_fields = ('data_criacao', 'ultima_atualizacao')  # Campos somente leitura


class AssinaturaClienteAdmin(admin.ModelAdmin):
    # Campos exibidos na lista de registros
    list_display = ('nome', 'email', 'plano', 'data_assinatura')
    list_filter = ('plano', 'data_assinatura')  # Filtros laterais
    search_fields = ('nome', 'email')  # Campos pesquisáveis
    ordering = ('-data_assinatura',)  # Ordenação padrão (do mais recente para o mais antigo)

    # Configuração do formulário detalhado
    fieldsets = (
        ('Informações do Cliente', {
            'fields': ('nome', 'email', 'telefone'),
        }),
        ('Detalhes do Plano', {
            'fields': ('plano',),
        }),
        ('Informações Adicionais', {
            'fields': ('data_assinatura',),
        }),
    )
    readonly_fields = ('data_assinatura',)  # Campos somente leitura


class ServicoAdmin(admin.ModelAdmin):
    # Campos exibidos na listagem
    list_display = ('nome', 'categoria', 'preco', 'ativo')
    # Filtros na barra lateral
    list_filter = ('categoria', 'ativo')
    # Campos pesquisáveis
    search_fields = ('nome', 'descricao')
    # Ordenação padrão
    ordering = ('categoria', 'nome')
    # Campos editáveis diretamente na lista
    list_editable = ('ativo',)


@admin.register(CategoriaLimite)
class CategoriaLimiteAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'limite')


admin.site.register(AssinaturaCliente, AssinaturaClienteAdmin)
admin.site.register(Assinatura, AssinaturaAdmin)
admin.site.register(Servico, ServicoAdmin)

# Register your models here.
admin.site.register(Reclamacao)


