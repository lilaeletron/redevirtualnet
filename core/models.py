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
    PLANO_CHOICES = [
        ('fibra_basico', 'Fibra Básico - 100Mbps'),
        ('fibra_intermediario', 'Fibra Intermediário - 300Mbps'),
        ('fibra_avancado', 'Fibra Avançado - 1Gbps'),
    ]

    plano = models.CharField(max_length=50, choices=PLANO_CHOICES)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    data_assinatura = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Assinatura {self.plano} de {self.nome}'
