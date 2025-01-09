# main/models.py
from django.db import models


class Reclamacao(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    reclamacao = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reclamação de {self.nome}'


class Assinatura(models.Model):
    # Choices para os tipos de assinatura
    TIPO_CHOICES = [
        ('combos', 'Combos'),
        ('internet', 'Planos de Internet'),
        ('tv', 'TV por Assinatura'),
        ('streaming', 'Pacote de Streamings'),
        ('controle', 'Plano Controle'),
        ('movel', 'Internet Móvel'),
        ('telemedicina', 'Telemedicina'),
        ('upgrades', 'Upgrades'),
    ]

    # Choices para os links predefinidos
    PAGINA_CHOICES = [
        ('wifi_turbo', 'Wi-Fi Turbo'),
        ('telemedicina', 'Telemedicina'),
        ('planos_internet', 'Planos de Internet'),
        ('tv_assinatura', 'TV por Assinatura'),
        ('streaming', 'Pacote de Streamings'),
        ('controle', 'Plano Controle'),
        ('nenhum', 'Nenhum Link'),  # Para quando não houver link associado
    ]

    # Campos gerais
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES, default='combos')
    nome = models.CharField(max_length=100)
    ordem = models.PositiveIntegerField(default=1)
    preco = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)  # Campo de preço adicionado

    # Descrições e links associados
    descricao1 = models.CharField(max_length=100, null=True, blank=True)  # Agora é CharField
    link1 = models.CharField(max_length=50, choices=PAGINA_CHOICES, default='nenhum')
    descricao2 = models.CharField(max_length=100, null=True, blank=True)
    link2 = models.CharField(max_length=50, choices=PAGINA_CHOICES, default='nenhum')
    descricao3 = models.CharField(max_length=100, null=True, blank=True)
    link3 = models.CharField(max_length=50, choices=PAGINA_CHOICES, default='nenhum')
    descricao4 = models.CharField(max_length=100, null=True, blank=True)
    link4 = models.CharField(max_length=50, choices=PAGINA_CHOICES, default='nenhum')
    descricao5 = models.CharField(max_length=100, null=True, blank=True)
    link5 = models.CharField(max_length=50, choices=PAGINA_CHOICES, default='nenhum')
    descricao6 = models.CharField(max_length=100, null=True, blank=True)
    link6 = models.CharField(max_length=50, choices=PAGINA_CHOICES, default='nenhum')
    descricao7 = models.CharField(max_length=100, null=True, blank=True)
    link7 = models.CharField(max_length=50, choices=PAGINA_CHOICES, default='nenhum')
    descricao8 = models.CharField(max_length=100, null=True, blank=True)
    link8 = models.CharField(max_length=50, choices=PAGINA_CHOICES, default='nenhum')
    descricao9 = models.CharField(max_length=100, null=True, blank=True)
    link9 = models.CharField(max_length=50, choices=PAGINA_CHOICES, default='nenhum')
    descricao10 = models.CharField(max_length=100, null=True, blank=True)
    link10 = models.CharField(max_length=50, choices=PAGINA_CHOICES, default='nenhum')

    # Controle de ativação e histórico
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()})"

    def descricoes_links(self):
        """
        Retorna uma lista de tuplas (descricao, link) contendo apenas as descrições preenchidas e seus links associados.
        Campos vazios são ignorados.

        Exemplo de retorno:
        [
            ("Descrição 1", "link1"),
            ("Descrição 2", "link2"),
            ...
        ]
        """
        descricoes_links = []  # Lista para armazenar as tuplas

        # Loop pelos índices das descrições e links (de 1 a 10)
        for i in range(1, 11):
            descricao = getattr(self, f"descricao{i}", None)  # Obtém o valor de descricao1, descricao2, ...
            link = getattr(self, f"link{i}", None)  # Obtém o valor de link1, link2, ...

            if descricao:  # Adiciona apenas se a descrição estiver preenchida
                descricoes_links.append((descricao, link or "nenhum"))  # 'nenhum' como padrão para link vazio

        return descricoes_links

    @property
    def descricoes(self):
        return [
            self.descricao1,
            self.descricao2,
            self.descricao3,
            self.descricao4,
            self.descricao5,
            self.descricao6,
            self.descricao7,
            self.descricao8,
            self.descricao9,
            self.descricao10
        ]

    @classmethod
    def tipos_unicos_ativos(cls):

        tipos_disponiveis = list(cls.objects.filter(ativo=True).values_list('tipo', flat=True).distinct())

        # Ordem personalizada
        ordem_personalizada = [
            'combos',
            'internet',
            'tv',
            'streaming',
            'controle',
            'movel',
            'telemedicina',
            'upgrades',
        ]

        return sorted(tipos_disponiveis, key=lambda tipo: ordem_personalizada.index(tipo) if tipo in ordem_personalizada else len(ordem_personalizada))


    @classmethod
    def assinaturas_por_tipo(cls):
        """Retorna um dicionário com assinaturas agrupadas por tipo."""
        tipos = cls.tipos_unicos_ativos()
        return {tipo: cls.objects.filter(tipo=tipo, ativo=True).order_by('ordem') for tipo in tipos}


class Servico(models.Model):
    # Categorias dos serviços
    CATEGORIA_CHOICES = [
        ('internet', 'Internet'),
        ('tv', 'TV'),
        ('streaming', 'Streaming'),
        ('telefonia', 'Telefonia'),
        ('chip_movel', 'Chip Móvel'),
        ('telemedicina', 'Telemedicina'),
        ('ponto_wifi', 'Ponto Wi-Fi 2.4G'),
        ('ip_gamer', 'IP Gamer'),
    ]

    # Campos do modelo
    nome = models.CharField(max_length=100, verbose_name="Nome do Serviço")
    categoria = models.CharField(
        max_length=50,
        choices=CATEGORIA_CHOICES,
        verbose_name="Categoria"
    )
    preco = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Preço (R$)"
    )
    descricao = models.TextField(
        null=True,
        blank=True,
        verbose_name="Descrição do Serviço"
    )
    ativo = models.BooleanField(default=True, verbose_name="Ativo")
    imagem = models.ImageField(
        upload_to='servicos/',
        null=True,
        blank=True,
        verbose_name="Imagem do Serviço"
    )
    destaque = models.BooleanField(default=False, verbose_name="Destaque")

    # Métodos
    def clean(self):
        # Validação para garantir que o preço seja positivo
        if self.preco <= 0:
            raise ValidationError("O preço deve ser maior que zero.")

    def __str__(self):
        return f"{self.nome} ({self.get_categoria_display()}) - R$ {self.preco:.2f}"

    class Meta:
        ordering = ['categoria', 'preco']
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"


class AssinaturaCliente(models.Model):
    plano = models.ForeignKey('Assinatura', on_delete=models.CASCADE, related_name='assinaturas')
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15, null=True, blank=True)
    data_assinatura = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.plano.nome}"


class CategoriaLimite(models.Model):
    # Supondo que você use as mesmas categorias definidas no modelo Servico
    CATEGORIA_CHOICES = [
        ('internet', 'Internet'),
        ('tv', 'TV'),
        ('telefonia', 'Telefonia'),
        ('chip_movel', 'Chip Móvel'),
        ('telemedicina', 'Telemedicina'),
        ('ponto_wifi', 'Ponto Wi-Fi 2.4G'),
        ('ip_gamer', 'IP Gamer'),
    ]

    categoria = models.CharField(
        max_length=50,
        choices=CATEGORIA_CHOICES,
        unique=True  # cada categoria só pode ter 1 registro de limite
    )
    limite = models.PositiveIntegerField(
        default=1,
        help_text="Quantos serviços desta categoria podem ser selecionados em um combo."
    )

    def __str__(self):
        return f"{self.get_categoria_display()} - Limite: {self.limite}"