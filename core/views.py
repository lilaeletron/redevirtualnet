# main/views.py
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ReclamacaoForm, AssinaturaClienteForm  # Você precisará criar esses formulários
from tools.load_image import ImageCarousel
from core.models import Assinatura, Servico, CategoriaLimite
import logging
from django.core import serializers

# Páginas Estáticas
logger = logging.getLogger(__name__)


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # Obtém o contexto padrão da superclasse
        context = super().get_context_data(**kwargs)

        # Atualiza o contexto com as variáveis necessárias
        context['carousel_images'] = ImageCarousel('.\core\static\img\carrossel').get_images()
        context['carousel_is_active'] = 2
        context['tipos'] = Assinatura.tipos_unicos_ativos()
        context['assinaturas'] = Assinatura.assinaturas_por_tipo()
        context['servicos'] = Servico.objects.filter(ativo=True).order_by('categoria', 'preco')

        # Log para depuração (remover em produção)
        logger.info("Tipos únicos ativos: %s", context['tipos'])
        logger.info("Assinaturas por tipo: %s", context['assinaturas'])

        return context


class QuemSomosView(TemplateView):
    template_name = 'quem_somos.html'


class MissaoVisaoValoresView(TemplateView):
    template_name = 'missao_visao_valores.html'


class InternetFibraView(TemplateView):
    template_name = 'internet_fibra.html'


class TelefoniaView(TemplateView):
    template_name = 'telefonia.html'


class TelemedicinaView(TemplateView):
    template_name = 'telemedicina.html'


class TVStreamingView(TemplateView):
    template_name = 'tv_streaming.html'


class CombosPersonalizadosView(TemplateView):
    template_name = 'combos_personalizados.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Todos os serviços ativos
        context['servicos'] = Servico.objects.filter(ativo=True).order_by('categoria', 'preco')
        context['combos'] = Assinatura.objects.filter(ativo=True, tipo='combos').order_by('ordem', 'preco')

        # Limites de cada categoria (vamos montar em um dicionário)
        limites_db = CategoriaLimite.objects.all()  # ex.: [CategoriaLimite(categoria="internet", limite=2), ...]
        limites_dict = {}
        for item in limites_db:
            limites_dict[item.categoria] = item.limite

        # Passar esse dict para o template
        context['limites_por_categoria'] = limites_dict

        context['servicos_test'] = serializers.serialize('json', context['servicos'])

        return context


class SimuladorPlanosView(TemplateView):
    template_name = 'simulador_planos.html'


class TesteVelocidadeView(TemplateView):
    template_name = 'teste_velocidade.html'


class FAQView(TemplateView):
    template_name = 'faq.html'


class SuporteTecnicoView(TemplateView):
    template_name = 'suporte_tecnico.html'


# Páginas com Formulários
class ReclamacoesView(FormView):
    template_name = 'reclamacoes.html'
    form_class = ReclamacaoForm
    success_url = reverse_lazy('reclamacoes')

    def form_valid(self, form):
        # Aqui você pode processar os dados do formulário
        form.save()
        return super().form_valid(form)


class AreaClienteView(LoginRequiredMixin, TemplateView):
    template_name = 'area_cliente.html'
    login_url = reverse_lazy('login')  # Defina a URL de login


class AssineAgoraView(TemplateView):
    template_name = 'main/assine_agora.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['planos'] = Assinatura.objects.filter(ativo=True).order_by('ordem')  # Apenas assinaturas ativas
        return context
