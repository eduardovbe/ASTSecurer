from ast_generator import *

def ast_load():
    with open('ast.json', 'r') as f:
        data = f.read()
    return json.loads(data)

def find_unused_variables(node):
    if isinstance(node, dict):
        # Verificar se o nó representa uma declaração de variável
        if node.get("node_type") == "VariableDeclaration":
            # Verificar se a variável é utilizada no código
            var_name = node.get("name")
            if not any(find_unused_variables(value) for value in node.values() if isinstance(value, (dict, list))) \
                    and not any(find_unused_variables(node) for node in ast_load() if node.get("node_type") == "Identifier" and node.get("name") == var_name):
                print("Variável declarada, mas não utilizada:", var_name)

        # Percorrer os filhos do nó
        for key, value in node.items():
            if isinstance(value, dict) or isinstance(value, list):
                find_unused_variables(value)
