# Generated by Django 4.2.17 on 2025-01-20 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_modal_alter_assinatura_link1_alter_assinatura_link10_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assinatura',
            name='link1',
            field=models.CharField(choices=[('wifi_turbo', '🌐 Com Wi-Fi Turbo'), ('sem_interrupcoes', '⚡ Sem Interrupções'), ('linha_telefonica', '📞 +01 Linha Telefônica'), ('atendimento_online', '📞 Atendimento 24h Online'), ('telemedicina', '💊 +01 Telemedicina Individual'), ('fibra_exclusivo', '📡 Exclusivo para Clientes Fibra'), ('acesso_ilimitado', '♾️ Acesso ilimitado'), ('streaming_pacotes', '🎥 Acesso a Max, Paramount+ e Watch Brasil'), ('max_dispositivos', '📱 Max: 3 Dispositivos'), ('watch_brasil_dispositivos', '📱 Watch Brasil: 4 Dispositivos'), ('nenhum', '🚧 Nenhum'), ('wifi_2_4g', '🌐 Wi-Fi 2.4G'), ('ip_fixo', '🌐 IP Fixo'), ('sva_escolha', '🎁 +01 SVA Da Sua Escolha')], default='🚧 Nenhum', max_length=50),
        ),
        migrations.AlterField(
            model_name='assinatura',
            name='link10',
            field=models.CharField(choices=[('wifi_turbo', '🌐 Com Wi-Fi Turbo'), ('sem_interrupcoes', '⚡ Sem Interrupções'), ('linha_telefonica', '📞 +01 Linha Telefônica'), ('atendimento_online', '📞 Atendimento 24h Online'), ('telemedicina', '💊 +01 Telemedicina Individual'), ('fibra_exclusivo', '📡 Exclusivo para Clientes Fibra'), ('acesso_ilimitado', '♾️ Acesso ilimitado'), ('streaming_pacotes', '🎥 Acesso a Max, Paramount+ e Watch Brasil'), ('max_dispositivos', '📱 Max: 3 Dispositivos'), ('watch_brasil_dispositivos', '📱 Watch Brasil: 4 Dispositivos'), ('nenhum', '🚧 Nenhum'), ('wifi_2_4g', '🌐 Wi-Fi 2.4G'), ('ip_fixo', '🌐 IP Fixo'), ('sva_escolha', '🎁 +01 SVA Da Sua Escolha')], default='🚧 Nenhum', max_length=50),
        ),
        migrations.AlterField(
            model_name='assinatura',
            name='link2',
            field=models.CharField(choices=[('wifi_turbo', '🌐 Com Wi-Fi Turbo'), ('sem_interrupcoes', '⚡ Sem Interrupções'), ('linha_telefonica', '📞 +01 Linha Telefônica'), ('atendimento_online', '📞 Atendimento 24h Online'), ('telemedicina', '💊 +01 Telemedicina Individual'), ('fibra_exclusivo', '📡 Exclusivo para Clientes Fibra'), ('acesso_ilimitado', '♾️ Acesso ilimitado'), ('streaming_pacotes', '🎥 Acesso a Max, Paramount+ e Watch Brasil'), ('max_dispositivos', '📱 Max: 3 Dispositivos'), ('watch_brasil_dispositivos', '📱 Watch Brasil: 4 Dispositivos'), ('nenhum', '🚧 Nenhum'), ('wifi_2_4g', '🌐 Wi-Fi 2.4G'), ('ip_fixo', '🌐 IP Fixo'), ('sva_escolha', '🎁 +01 SVA Da Sua Escolha')], default='🚧 Nenhum', max_length=50),
        ),
        migrations.AlterField(
            model_name='assinatura',
            name='link3',
            field=models.CharField(choices=[('wifi_turbo', '🌐 Com Wi-Fi Turbo'), ('sem_interrupcoes', '⚡ Sem Interrupções'), ('linha_telefonica', '📞 +01 Linha Telefônica'), ('atendimento_online', '📞 Atendimento 24h Online'), ('telemedicina', '💊 +01 Telemedicina Individual'), ('fibra_exclusivo', '📡 Exclusivo para Clientes Fibra'), ('acesso_ilimitado', '♾️ Acesso ilimitado'), ('streaming_pacotes', '🎥 Acesso a Max, Paramount+ e Watch Brasil'), ('max_dispositivos', '📱 Max: 3 Dispositivos'), ('watch_brasil_dispositivos', '📱 Watch Brasil: 4 Dispositivos'), ('nenhum', '🚧 Nenhum'), ('wifi_2_4g', '🌐 Wi-Fi 2.4G'), ('ip_fixo', '🌐 IP Fixo'), ('sva_escolha', '🎁 +01 SVA Da Sua Escolha')], default='🚧 Nenhum', max_length=50),
        ),
        migrations.AlterField(
            model_name='assinatura',
            name='link4',
            field=models.CharField(choices=[('wifi_turbo', '🌐 Com Wi-Fi Turbo'), ('sem_interrupcoes', '⚡ Sem Interrupções'), ('linha_telefonica', '📞 +01 Linha Telefônica'), ('atendimento_online', '📞 Atendimento 24h Online'), ('telemedicina', '💊 +01 Telemedicina Individual'), ('fibra_exclusivo', '📡 Exclusivo para Clientes Fibra'), ('acesso_ilimitado', '♾️ Acesso ilimitado'), ('streaming_pacotes', '🎥 Acesso a Max, Paramount+ e Watch Brasil'), ('max_dispositivos', '📱 Max: 3 Dispositivos'), ('watch_brasil_dispositivos', '📱 Watch Brasil: 4 Dispositivos'), ('nenhum', '🚧 Nenhum'), ('wifi_2_4g', '🌐 Wi-Fi 2.4G'), ('ip_fixo', '🌐 IP Fixo'), ('sva_escolha', '🎁 +01 SVA Da Sua Escolha')], default='🚧 Nenhum', max_length=50),
        ),
        migrations.AlterField(
            model_name='assinatura',
            name='link5',
            field=models.CharField(choices=[('wifi_turbo', '🌐 Com Wi-Fi Turbo'), ('sem_interrupcoes', '⚡ Sem Interrupções'), ('linha_telefonica', '📞 +01 Linha Telefônica'), ('atendimento_online', '📞 Atendimento 24h Online'), ('telemedicina', '💊 +01 Telemedicina Individual'), ('fibra_exclusivo', '📡 Exclusivo para Clientes Fibra'), ('acesso_ilimitado', '♾️ Acesso ilimitado'), ('streaming_pacotes', '🎥 Acesso a Max, Paramount+ e Watch Brasil'), ('max_dispositivos', '📱 Max: 3 Dispositivos'), ('watch_brasil_dispositivos', '📱 Watch Brasil: 4 Dispositivos'), ('nenhum', '🚧 Nenhum'), ('wifi_2_4g', '🌐 Wi-Fi 2.4G'), ('ip_fixo', '🌐 IP Fixo'), ('sva_escolha', '🎁 +01 SVA Da Sua Escolha')], default='🚧 Nenhum', max_length=50),
        ),
        migrations.AlterField(
            model_name='assinatura',
            name='link6',
            field=models.CharField(choices=[('wifi_turbo', '🌐 Com Wi-Fi Turbo'), ('sem_interrupcoes', '⚡ Sem Interrupções'), ('linha_telefonica', '📞 +01 Linha Telefônica'), ('atendimento_online', '📞 Atendimento 24h Online'), ('telemedicina', '💊 +01 Telemedicina Individual'), ('fibra_exclusivo', '📡 Exclusivo para Clientes Fibra'), ('acesso_ilimitado', '♾️ Acesso ilimitado'), ('streaming_pacotes', '🎥 Acesso a Max, Paramount+ e Watch Brasil'), ('max_dispositivos', '📱 Max: 3 Dispositivos'), ('watch_brasil_dispositivos', '📱 Watch Brasil: 4 Dispositivos'), ('nenhum', '🚧 Nenhum'), ('wifi_2_4g', '🌐 Wi-Fi 2.4G'), ('ip_fixo', '🌐 IP Fixo'), ('sva_escolha', '🎁 +01 SVA Da Sua Escolha')], default='🚧 Nenhum', max_length=50),
        ),
        migrations.AlterField(
            model_name='assinatura',
            name='link7',
            field=models.CharField(choices=[('wifi_turbo', '🌐 Com Wi-Fi Turbo'), ('sem_interrupcoes', '⚡ Sem Interrupções'), ('linha_telefonica', '📞 +01 Linha Telefônica'), ('atendimento_online', '📞 Atendimento 24h Online'), ('telemedicina', '💊 +01 Telemedicina Individual'), ('fibra_exclusivo', '📡 Exclusivo para Clientes Fibra'), ('acesso_ilimitado', '♾️ Acesso ilimitado'), ('streaming_pacotes', '🎥 Acesso a Max, Paramount+ e Watch Brasil'), ('max_dispositivos', '📱 Max: 3 Dispositivos'), ('watch_brasil_dispositivos', '📱 Watch Brasil: 4 Dispositivos'), ('nenhum', '🚧 Nenhum'), ('wifi_2_4g', '🌐 Wi-Fi 2.4G'), ('ip_fixo', '🌐 IP Fixo'), ('sva_escolha', '🎁 +01 SVA Da Sua Escolha')], default='🚧 Nenhum', max_length=50),
        ),
        migrations.AlterField(
            model_name='assinatura',
            name='link8',
            field=models.CharField(choices=[('wifi_turbo', '🌐 Com Wi-Fi Turbo'), ('sem_interrupcoes', '⚡ Sem Interrupções'), ('linha_telefonica', '📞 +01 Linha Telefônica'), ('atendimento_online', '📞 Atendimento 24h Online'), ('telemedicina', '💊 +01 Telemedicina Individual'), ('fibra_exclusivo', '📡 Exclusivo para Clientes Fibra'), ('acesso_ilimitado', '♾️ Acesso ilimitado'), ('streaming_pacotes', '🎥 Acesso a Max, Paramount+ e Watch Brasil'), ('max_dispositivos', '📱 Max: 3 Dispositivos'), ('watch_brasil_dispositivos', '📱 Watch Brasil: 4 Dispositivos'), ('nenhum', '🚧 Nenhum'), ('wifi_2_4g', '🌐 Wi-Fi 2.4G'), ('ip_fixo', '🌐 IP Fixo'), ('sva_escolha', '🎁 +01 SVA Da Sua Escolha')], default='🚧 Nenhum', max_length=50),
        ),
        migrations.AlterField(
            model_name='assinatura',
            name='link9',
            field=models.CharField(choices=[('wifi_turbo', '🌐 Com Wi-Fi Turbo'), ('sem_interrupcoes', '⚡ Sem Interrupções'), ('linha_telefonica', '📞 +01 Linha Telefônica'), ('atendimento_online', '📞 Atendimento 24h Online'), ('telemedicina', '💊 +01 Telemedicina Individual'), ('fibra_exclusivo', '📡 Exclusivo para Clientes Fibra'), ('acesso_ilimitado', '♾️ Acesso ilimitado'), ('streaming_pacotes', '🎥 Acesso a Max, Paramount+ e Watch Brasil'), ('max_dispositivos', '📱 Max: 3 Dispositivos'), ('watch_brasil_dispositivos', '📱 Watch Brasil: 4 Dispositivos'), ('nenhum', '🚧 Nenhum'), ('wifi_2_4g', '🌐 Wi-Fi 2.4G'), ('ip_fixo', '🌐 IP Fixo'), ('sva_escolha', '🎁 +01 SVA Da Sua Escolha')], default='🚧 Nenhum', max_length=50),
        ),
    ]
