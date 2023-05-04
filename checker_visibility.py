def find_default_visibilities(node):
    default_visibilities = []
    try:
        # Percorre a AST buscando por declarações de variáveis e funções
        if isinstance(node, dict) and node["type"] == 'VariableDeclaration':
            # Se a visibilidade não for definida, adiciona à lista
            if node["visibility"] == "default":
                default_visibilities.append(f"Variável :{node['name']}")
        elif isinstance(node, dict) and node["type"] == 'FunctionDefinition':
            # Se a visibilidade não for definida, adiciona à lista
            if node["visibility"] == "default":
                default_visibilities.append(f"Função :{node['name']}")
    except Exception as E:
        pass
    for key, value in node.items():
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    default_visibilities.extend(find_default_visibilities(item))
        elif isinstance(value, dict):
            default_visibilities.extend(find_default_visibilities(value))

    return default_visibilities