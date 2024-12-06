import os


def generate_tree(dir_path, prefix=''):
    """Gera e imprime a estrutura de pastas recursivamente, excluindo itens ocultos."""
    try:
        # Lista os itens no diretório atual, excluindo itens ocultos
        items = sorted([item for item in os.listdir(dir_path) if not item.startswith('.')])
    except PermissionError:
        print(prefix + "└── [Permissão Negada]")
        return
    total_items = len(items)

    for index, item in enumerate(items):
        path = os.path.join(dir_path, item)
        connector = '├── ' if index < total_items - 1 else '└── '
        print(prefix + connector + item)

        if os.path.isdir(path):
            # Define o prefixo para os subníveis
            extension = '│   ' if index < total_items - 1 else '    '
            generate_tree(path, prefix + extension)


if __name__ == "__main__":
    # Define o diretório inicial como a raiz do projeto
    start_dir = os.path.abspath('./..')
    project_name = os.path.basename(start_dir)
    print(project_name + '/')
    generate_tree(start_dir)
