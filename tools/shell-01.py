from core.models import Assinatura

# Plano Básico
Assinatura.objects.create(
    tipo="internet",
    nome="Plano Básico - 75 Mega",
    ordem=1,
    descricao1="🛜 Wi-Fi 2.4G",
    descricao2="♾️ Acesso ilimitado",
    descricao3="🔄 Conexão Estável",
    descricao4="📞 Atendimento 24h Online",
    preco=55.00,
    ativo=True
)

# Plano Intermediário
Assinatura.objects.create(
    tipo="internet",
    nome="Plano Intermediário - 150 Mega",
    ordem=2,
    descricao1="🛜 Wi-Fi 2.4G",
    descricao2="🛜 Wi-Fi 5.0G",
    descricao3="♾️ Acesso ilimitado",
    descricao4="🔄 Conexão Estável",
    descricao5="📞 Atendimento 24h Online",
    preco=80.00,
    ativo=True
)

# Plano Avançado
Assinatura.objects.create(
    tipo="internet",
    nome="Plano Avançado - 300 Mega",
    ordem=3,
    descricao1="🛜 Wi-Fi 2.4G",
    descricao2="🛜 Wi-Fi 5.0G",
    descricao3="♾️ Acesso ilimitado",
    descricao4="🔄 Conexão Estável",
    descricao5="📞 Atendimento 24h Online",
    preco=100.00,
    ativo=True
)

# Plano Premium
Assinatura.objects.create(
    tipo="internet",
    nome="Plano Premium - 500 Mega",
    ordem=4,
    descricao1="🛜 Wi-Fi 2.4G",
    descricao2="🛜 Wi-Fi 5.0G",
    descricao3="♾️ Acesso ilimitado",
    descricao4="🔄 Conexão Estável",
    descricao5="📞 Atendimento 24h Online",
    preco=120.00,
    ativo=True
)

# Plano Top
Assinatura.objects.create(
    tipo="internet",
    nome="Plano Top - 1 Giga",
    ordem=5,
    descricao1="🛜 Wi-Fi 2.4G",
    descricao2="🛜 Wi-Fi 5.0G",
    descricao3="♾️ Acesso ilimitado",
    descricao4="🔄 Conexão Estável",
    descricao5="📞 Atendimento 24h Online",
    preco=134.90,
    ativo=True
)

# Plano Top
Assinatura.objects.create(
    tipo="internet",
    nome="Plano Gamer - 1 Giga",
    ordem=5,
    descricao1="🛜 Wi-Fi 2.4G",
    descricao2="🛜 Wi-Fi 5.0G",
    descricao3="🎮 IP Fixo para Gamers",
    descricao4="♾️ Acesso ilimitado",
    descricao5="🔄 Conexão Estável",
    descricao6="📞 Atendimento 24h Online",
    preco=134.90,
    ativo=True
)