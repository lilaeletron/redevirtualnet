# main/urls.py
from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('quem-somos/', views.QuemSomosView.as_view(), name='quem_somos'),
    path('missao-visao-valores/', views.MissaoVisaoValoresView.as_view(), name='missao_visao_valores'),

    # Planos
    path('planos/internet-fibra/', views.InternetFibraView.as_view(), name='internet_fibra'),
    path('planos/telefonia/', views.TelefoniaView.as_view(), name='telefonia'),
    path('planos/telemedicina/', views.TelemedicinaView.as_view(), name='telemedicina'),
    path('planos/tv-streaming/', views.TVStreamingView.as_view(), name='tv_streaming'),
    path('planos/combos-personalizados/', views.CombosPersonalizadosView.as_view(), name='combos_personalizados'),

    # Ferramentas
    path('ferramentas/simulador-planos/', views.SimuladorPlanosView.as_view(), name='simulador_planos'),
    path('ferramentas/teste-velocidade/', views.TesteVelocidadeView.as_view(), name='teste_velocidade'),

    # Suporte
    path('suporte/faq/', views.FAQView.as_view(), name='faq'),
    path('suporte/suporte-tecnico/', views.SuporteTecnicoView.as_view(), name='suporte_tecnico'),
    path('suporte/reclamacoes/', views.ReclamacoesView.as_view(), name='reclamacoes'),

    # Área do Cliente e Assine Agora
    path('area-cliente/', views.AreaClienteView.as_view(), name='area_cliente'),
    path('assine-agora/', views.AssineAgoraView.as_view(), name='assine_agora'),
]

