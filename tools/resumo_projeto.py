import os
import ast
from ollama import Client  # Importa a classe Client para configurar o Ollama

# Extensões de arquivos que serão analisados
EXTENSOES_RELEVANTES = {'.py', '.html', '.css', '.js'}

# Pastas que serão ignoradas durante a análise
PASTAS_IGNORADAS = {'__pycache__', '.git', '.venv', 'node_modules'}

# Host remoto do servidor Ollama
OLLAMA_HOST = "http://45.229.53.169:11434"  # Altere para o IP/host correto
MODELO_OLLAMA = "llama3.2"  # Modelo padrão para análise


def escanear_diretorio(diretorio_base):
    """
    Escaneia o diretório base e retorna uma lista de caminhos de arquivos relevantes.
    """
    arquivos_relevantes = []

    for root, dirs, files in os.walk(diretorio_base):
        # Filtra as pastas a serem ignoradas
        dirs[:] = [d for d in dirs if d not in PASTAS_IGNORADAS]

        # Adiciona arquivos com extensões relevantes
        for file in files:
            if os.path.splitext(file)[1] in EXTENSOES_RELEVANTES:
                arquivos_relevantes.append(os.path.join(root, file))

    return arquivos_relevantes


def gerar_resumo_ollama(conteudo, arquivo, cliente_ollama, modelo=MODELO_OLLAMA):
    """
    Gera um resumo do conteúdo do arquivo utilizando o cliente Ollama.

    Fornece instruções específicas para evitar relatórios com raciocínio expansivo.
    """
    extensao = os.path.splitext(arquivo)[1]

    # Prompt ajustado para evitar <think> ou explicações desnecessárias
    if extensao == '.py':
        user_prompt = (
            f"Resuma o código Python do arquivo {arquivo} de forma direta e objetiva. "
            f"Apenas descreva o que o arquivo faz, sem incluir explicações descritivas sobre meu raciocínio. "
            f"Liste também as funções definidas e chamadas, conforme aplicável.\n\n{conteudo}"
        )
    else:
        user_prompt = (
            f"Resuma o conteúdo do arquivo {arquivo} de forma objetiva, descrevendo apenas a funcionalidade geral, "
            f"sem explicar os passos do seu raciocínio ou pensamento.\n\n{conteudo}"
        )

    system_message = {
        'role': 'system',
        'content': (
            "Você é um assistente que gera resumos concisos de código e documentos. "
            "Não inclua descrições sobre como você pensou ou analisou o conteúdo; "
            "apenas forneça o resumo diretamente."
        )
    }

    user_message = {
        'role': 'user',
        'content': user_prompt
    }

    try:
        resposta = cliente_ollama.chat(model=modelo, messages=[system_message, user_message])
        resumo = resposta.message.content
        return resumo if resumo else None

    except Exception as e:
        print(f"Erro ao se conectar ao modelo Ollama para o arquivo {arquivo}: {e}")
        return None


def analisar_funcoes_codigo(arquivo):
    """
    Analisa um arquivo Python para identificar funções definidas, chamadas e não usadas.
    """
    try:
        with open(arquivo, 'r', encoding='utf-8', errors='ignore') as f:
            codigo = f.read()

        arvore = ast.parse(codigo)  # Analisa o código Python como uma AST
        funcoes_definidas = []
        funcoes_chamadas = set()

        for node in ast.walk(arvore):
            if isinstance(node, ast.FunctionDef):  # Funções definidas
                funcoes_definidas.append(node.name)
            elif isinstance(node, ast.Call):  # Funções chamadas
                if isinstance(node.func, ast.Name):
                    funcoes_chamadas.add(node.func.id)

        # Identifica funções definidas, mas não chamadas
        funcoes_nao_usadas = [f for f in funcoes_definidas if f not in funcoes_chamadas]

        return {
            "definidas": funcoes_definidas,
            "chamadas": list(funcoes_chamadas),
            "nao_usadas": funcoes_nao_usadas
        }

    except Exception as e:
        print(f"Erro ao analisar funções no arquivo {arquivo}: {e}")
        return None


def processar_arquivos(arquivos, arquivo_saida, cliente_ollama, modelo):
    """
    Processa uma lista de arquivos, gera resumos e salva os resultados em um arquivo texto.
    """
    with open(arquivo_saida, 'w', encoding='utf-8') as resumo_txt:
        for arquivo in arquivos:
            try:
                # Lê o conteúdo do arquivo
                with open(arquivo, 'r', encoding='utf-8', errors='ignore') as f:
                    conteudo = f.read()

                # Ignora arquivos sem conteúdo
                if not conteudo.strip():
                    print(f"Arquivo ignorado (sem conteúdo): {arquivo}")
                    continue

                print(f"Gerando resumo para o arquivo: {arquivo}...")

                resumo = gerar_resumo_ollama(conteudo, arquivo, cliente_ollama, modelo)

                if resumo:
                    resumo_txt.write(f"Arquivo: {arquivo}\n")
                    resumo_txt.write(f"Resumo:\n{resumo}\n")

                    # Para arquivos Python, realiza análise adicional das funções
                    if arquivo.endswith('.py'):
                        analise_funcoes = analisar_funcoes_codigo(arquivo)

                        if analise_funcoes:
                            resumo_txt.write("\nCadeia de Funções:\n")
                            resumo_txt.write(f"- Funções Definidas: {analise_funcoes['definidas']}\n")
                            resumo_txt.write(f"- Funções Chamadas: {analise_funcoes['chamadas']}\n")
                            resumo_txt.write(f"- Funções Não Usadas: {analise_funcoes['nao_usadas']}\n")

                    resumo_txt.write("=" * 80 + "\n")  # Separador entre resumos

            except Exception as e:
                print(f"Erro ao processar o arquivo {arquivo}: {e}")


def principal():
    """
    Função principal: coordena a execução do script.
    """
    diretorio_base = input("Digite o caminho do diretório base: ")

    if not os.path.exists(diretorio_base):
        print("O diretório fornecido não existe.")
        return

    # Configura o cliente Ollama
    print(f"Conectando ao servidor Ollama em {OLLAMA_HOST}...")
    cliente_ollama = Client(host=OLLAMA_HOST)

    modelo = input(f"Digite o modelo Ollama a ser utilizado (padrão: {MODELO_OLLAMA}): ") or MODELO_OLLAMA

    print("Escaneando o diretório...")
    arquivos_relevantes = escanear_diretorio(diretorio_base)

    if not arquivos_relevantes:
        print("Nenhum arquivo relevante foi encontrado.")
        return

    # Define o caminho do arquivo de saída
    arquivo_saida = os.path.join(diretorio_base, "resumo_projeto.txt")

    processar_arquivos(arquivos_relevantes, arquivo_saida, cliente_ollama, modelo)

    print(f"Resumos gerados e salvos em: {arquivo_saida}")


if __name__ == '__main__':
    principal()
