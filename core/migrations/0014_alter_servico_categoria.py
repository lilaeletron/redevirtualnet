# Generated by Django 4.2.17 on 2025-01-08 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_categorialimite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='categoria',
            field=models.CharField(choices=[('internet', 'Internet'), ('tv', 'TV'), ('streaming', 'Streaming'), ('telefonia', 'Telefonia'), ('chip_movel', 'Chip Móvel'), ('telemedicina', 'Telemedicina'), ('ponto_wifi', 'Ponto Wi-Fi 2.4G'), ('ip_gamer', 'IP Gamer')], max_length=50, verbose_name='Categoria'),
        ),
    ]
