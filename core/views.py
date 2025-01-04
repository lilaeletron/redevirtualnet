# main/views.py
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ReclamacaoForm, AssinaturaForm  # Você precisará criar esses formulários
from tools.load_image import ImageCarousel


# Páginas Estáticas
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # Obtém o contexto padrão da superclasse
        context = super().get_context_data(**kwargs)

        context.update({
            'carousel_images': ImageCarousel('.\core\static\img').get_images(),
            'carousel_is_active': 2,
        })

        return context

    def __str__(self):
        return "IndexView"


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


class AssineAgoraView(FormView):
    template_name = 'assine_agora.html'
    form_class = AssinaturaForm
    success_url = reverse_lazy('assine_agora')

    def form_valid(self, form):
        # Processar a assinatura
        form.save()
        return super().form_valid(form)
