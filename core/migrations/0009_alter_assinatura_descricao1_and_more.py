# Generated by Django 4.2.17 on 2025-01-07 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_assinaturacliente_delete_combo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assinatura',
            name='descricao1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assinatura',
            name='descricao10',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assinatura',
            name='descricao2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assinatura',
            name='descricao3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assinatura',
            name='descricao4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assinatura',
            name='descricao5',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assinatura',
            name='descricao6',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assinatura',
            name='descricao7',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assinatura',
            name='descricao8',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assinatura',
            name='descricao9',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
