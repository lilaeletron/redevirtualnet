import os
import time
import subprocess


INTERVAL = 5;
while True:
    print("Verificando por atualizações remotas...")

    # Busca atualizações do repositório remoto
    subprocess.run(["git", "fetch", "origin"], check=True)

    # Verifica se há atualizações
    status = subprocess.run(["git", "status", "-uno"], capture_output=True, text=True)
    if "Your branch is behind" in status.stdout:
        print("Atualizações detectadas! Aplicando...")
        subprocess.run(["git", "pull", "origin", "main"], check=True)
        print("Atualizações aplicadas com sucesso!")
    else:
        print("Nenhuma atualização encontrada.")

    # Aguardar antes da próxima verificação
    time.sleep(INTERVAL)