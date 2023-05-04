DEPRECATED_FUNCTIONS = ["suicide", "sha3()", "throw", "gasleft","block.blockhash","callcode","msg.gas"]

def find_deprecated_functions(node):
    deprecated_functions = []
    try:
        # Verificando se o nó atual contém a chamada a funções depreciadas
        if isinstance(node, dict) and node.get('type') == 'FunctionCall' and node['expression'].get(
                'name') in DEPRECATED_FUNCTIONS:
            deprecated_functions.append(node['expression'].get(
                'name'))
    except Exception as E:
        pass
    # Percorrendo os filhos do nó atual
    for key, value in node.items():
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    deprecated_functions.extend(find_deprecated_functions(item))
        elif isinstance(value, dict):
            deprecated_functions.extend(find_deprecated_functions(value))

    return deprecated_functions