import sys
import json
import solidity_parser
import re
import os

# Funções procuradas
DEPRECATED_FUNCTIONS = ["suicide", "sha3()", "throw", "gasleft"]
# Caminho e nome do contrato inteligente
SOLIDITY_FILE_PATH = "unchecked_low_level_calls/0x7d09edb07d23acb532a82be3da5c17d9d85806b4.sol"


def open_file_and_save():
    with open(SOLIDITY_FILE_PATH, "r") as file:
        solidity_code = file.read()
    ast = solidity_parser.parse(solidity_code)
    ast_json = json.dumps(ast, indent=4)
    file.close()
    with open('ast.json', 'w') as f:
        f.write(ast_json)
        f.close()
    with open('ast.json', 'r') as f:
        data = f.read()
    return json.loads(data)


def search_deprecated_functions(node):
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
                    deprecated_functions.extend(search_deprecated_functions(item))
        elif isinstance(value, dict):
            deprecated_functions.extend(search_deprecated_functions(value))

    return deprecated_functions


def find_default_visibilities(node):
    default_visibilities = []
    try:
        # Percorre a AST buscando por declarações de variáveis e funções
        if isinstance(node, dict) and node["type"] == 'VariableDeclaration':
            # Se a visibilidade não for definida, adiciona à lista
            if node["visibility"] == "default":
                default_visibilities.append({
                    'type': 'variável',
                    'nome': node["name"],
                })
        elif isinstance(node, dict) and node["type"] == 'FunctionDefinition':
            # Se a visibilidade não for definida, adiciona à lista
            if node["visibility"] == "default":
                default_visibilities.append({
                    'type': 'função',
                    'nome': node["name"]
                })
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


def verify_version(node):
    text_version = node["children"][0]["value"]
    version = re.findall(r"\d+\.\d+\.\d+", text_version)
    outdate = False
    if int(version[-1][2]) < 8:
        outdate = True

    return outdate, version[-1]


def find_transfer_or_send(node):
    transfer_or_send = []
    if isinstance(node, dict) and node.get('type') == 'FunctionCall':
        function_name = node['expression'].get('memberName')
        if function_name == 'transfer' or function_name == 'send':
            transfer_or_send.append(function_name)
    for key, value in node.items():
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    transfer_or_send.extend(find_transfer_or_send(item))
        elif isinstance(value, dict):
            transfer_or_send.extend(find_transfer_or_send(value))
    return transfer_or_send


def has_unchecked_calls(node, find=0):
    unchecked_calls = []
    if isinstance(node, dict) and node.get("expression") is not None:
        if node['expression'].get('name') == 'require' or node['expression'].get('name') == 'assert':
            find = 4
    if find > 0:
        find -= 1
    try:
        if isinstance(node, dict) and (node.get('type') == 'FunctionCall' or node.get('type') == 'MemberAccess') \
                and node['expression'].get('name') != 'require' \
                and node['expression'].get('name') != 'assert' \
                and node['expression'].get('memberName') == 'call' \
                and find == 0:
            unchecked_calls.append(node['expression']['expression'].get("name"))
        for key, value in node.items():
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        unchecked_calls.extend(has_unchecked_calls(item, find=find))
            elif isinstance(value, dict):
                unchecked_calls.extend(has_unchecked_calls(value, find=find))
        return unchecked_calls
    except:
        pass


def verify_all():
    search = search_deprecated_functions(ast)
    search2 = find_default_visibilities(ast)
    search3, version = verify_version(ast)
    search4 = find_transfer_or_send(ast)
    search5 = has_unchecked_calls(ast)

    if len(search5) > 0:
        print("SWC-104 Foram encontrados valores de retorno de chamada sem controle:")
        print(search5)

    if search3:
        print("SWC-100 O código funciona em uma versão do solidity antiga")
        print(f"Versão =  {version}")

    if len(search) > 0:
        print("SWC-111 Foram encontrados as seguintes funções depreciadas:")
        for item in search:
            print(item)

    if len(search) > 0:
        print("SWC-102 Foram encontrados as seguintes funções e variveis sem visibilidade declarada:")
        for item in search2:
            print(f"Tipo : {item['type']} , Nome : {item['nome']}")

    if len(search4) > 0:
        print("SWC-134 Foram encontrados send() ou transfer() no código:")
        for item in search4:
            print(item)





if __name__ == "__main__":
    path = 'unchecked_low_level_calls/'
    arquivos = []
    for nome_arquivo in os.listdir(path):
        if os.path.isfile(os.path.join(path, nome_arquivo)):
            arquivos.append(nome_arquivo)

    for arq in arquivos:
        SOLIDITY_FILE_PATH = path + arq
        # Carrega o arquivo e salva a ast em formato json
        ast = open_file_and_save()
        print(arq)
        # Percorre a AST e procurando vulnerabilidades
        verify_all()
