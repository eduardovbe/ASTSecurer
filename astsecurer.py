import os
import sys
from colorama import Fore, Style
from abstract_tree.ast_generator import *
from vulnerabilities.code_version_checker import *
from vulnerabilities.depreciated_checker import *
from vulnerabilities.unchecked_calls_checker import *
from vulnerabilities.visibility_checker import *
from vulnerabilities.assembly_code_checker import *
from vulnerabilities.txorigin_checker import *
from vulnerabilities.block_values_checker import *
from vulnerabilities.Right_To_Left_Override_checker import *
from vulnerabilities.unused_variable_checker import *

default_colors = {
    "safe": Fore.LIGHTGREEN_EX,
    "warning": Fore.LIGHTRED_EX,
    "result": Fore.LIGHTYELLOW_EX,
    "c_name": Fore.LIGHTBLUE_EX
}


def unused_variable(ast):
    result = find_unused_variable(ast)
    if result:
        print(
            default_colors[
                "warning"] + "SWC-131 Variaveis não utilizadas encontrado no código:" + Style.RESET_ALL)
        print(default_colors["result"] + str(result) + Style.RESET_ALL)
        return True
    else:
        return False


def right_to_left_override(ast):
    result = find_rtl_override_control_character(ast)
    if result:
        print(
            default_colors[
                "warning"] + "SWC-130 Right-To-Left-Override control character (U+202E) encontrado no código:" + Style.RESET_ALL)
        print(default_colors["result"] + r"\u202E" + Style.RESET_ALL)
        return True
    else:
        return False


def visibility(ast):
    result = find_default_visibilities(ast)
    if len(result) > 0:
        list_str = list(map(str, result))
        result = ', '.join(list_str)
        print(
            default_colors[
                "warning"] + "SWC-100/SWC-108 Foram encontrados as seguintes funções e variveis sem visibilidade declarada:" + Style.RESET_ALL)
        print(default_colors["result"] + str(result) + Style.RESET_ALL)
        return True
    else:
        return False


def deprecated_functions(ast):
    result = find_deprecated_functions(ast)
    if len(result) > 0:
        list_str = list(map(str, result))
        result = ', '.join(list_str)
        print(
            default_colors["warning"] + "SWC-111 Foram encontrados as seguintes funções depreciadas:" + Style.RESET_ALL)
        print(default_colors["result"] + str(result) + Style.RESET_ALL)
        return True
    else:
        return False


def tx_origin(ast):
    result = find_tx_origin(ast)
    if result is not None:
        if len(result) > 0:
            list_str = list(map(str, result))
            result = ', '.join(list_str)
            print(
                default_colors["warning"] + "SWC-115 Tx.Origin utilizado no contexto errado:" + Style.RESET_ALL)
            print(default_colors["result"] + str(result) + Style.RESET_ALL)
            return True
        else:
            return False


def block_values(ast):
    result = find_block_properties(ast)
    if len(result) > 0:
        list_str = list(map(str, result))
        result = ', '.join(list_str)
        print(
            default_colors[
                "warning"] + "SWC-116 As funcionalidades são dependentes de tempos de blocos:" + Style.RESET_ALL)
        print(default_colors["result"] + str(result) + Style.RESET_ALL)
        return True
    else:
        return False


def old_version(ast):
    result = find_old_version(ast)
    if len(result) > 0:
        print(
            default_colors["warning"] + "SWC-102 O código funciona em uma versão do solidity antiga" + Style.RESET_ALL)
        print(default_colors["result"] + f"Versão =  {result}" + Style.RESET_ALL)
        return True
    else:
        return False


def assembly_code(ast):
    result = find_assembly(ast)
    if len(result) > 0:
        list_str = list(map(str, result))
        result = ', '.join(list_str)
        print(default_colors["warning"] + "SWC-127 Foram encontrados código em assembly no código que podem "
                                          "ocasionar vulnerabilidades:" + Style.RESET_ALL)
        print(default_colors["result"] + str(result) + Style.RESET_ALL)
        return True
    else:
        return False


def unchecked_calls(ast):
    result = find_unchecked_calls(ast)
    if len(result) > 0:
        list_str = list(map(str, result))
        result = ', '.join(list_str)
        print(
            default_colors[
                "warning"] + "SWC-104 Foram encontrados valores de retorno de chamada sem controle:" + Style.RESET_ALL)
        print(default_colors["result"] + result + Style.RESET_ALL)
        return True
    else:
        return False


def verify_all(ast):
    verifications = [visibility, deprecated_functions, unchecked_calls,
                     assembly_code, tx_origin, block_values, right_to_left_override, unused_variable]
    find = False
    for verify in verifications:
        result = verify(ast)
        if result:
            find = True
    if find:
        return True
    else:
        return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("É necessário fornecer o diretório do dataset como argumento.")
        exit()
    path = sys.argv[1]
    arquivos = []
    for nome_arquivo in os.listdir(path):
        if os.path.isfile(os.path.join(path, nome_arquivo)):
            if nome_arquivo.endswith(".sol"):
                arquivos.append(nome_arquivo)
    for arq in arquivos:
        SOLIDITY_FILE_PATH = path +"/"+ arq
        ast = open_file_and_save(SOLIDITY_FILE_PATH)
        print(default_colors["c_name"] + arq + Style.RESET_ALL)
        not_safe = verify_all(ast)
        if not not_safe:
            print(default_colors["safe"] + "Não encontrados vulnerabilidades nesse contrato" + Style.RESET_ALL)
