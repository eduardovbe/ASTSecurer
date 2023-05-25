from abstract_tree.ast_generator import *


def ast_load():
    with open('ast.json', 'r') as f:
        data = f.read()
    return json.loads(data)


def find_unused_variable(node):
    skip = 0
    list_unused_variable = []
    if isinstance(node, dict):
        if node.get("type") == "StructDefinition":
            skip = 1
        if node.get("type") == "VariableDeclaration":
            var_name = node.get("name")
            ast = ast_load()
            if not verify_variable(ast, var_name):
                list_unused_variable.append(var_name)
    for key, value in node.items():
        if isinstance(value, list) and skip == 0:
            for item in value:
                if isinstance(item, dict):
                    list_unused_variable.extend(find_unused_variable(item))
        elif isinstance(value, dict) and skip == 0:
            list_unused_variable.extend(find_unused_variable(value))
    return list_unused_variable


def verify_variable(node, indentity):
    skip = 0
    if isinstance(node, dict):
        if node.get("BinaryOperation") is not None:
            if node.get("BinaryOperation").get("left").get("name") == indentity:
                skip = 1
        if node.get("type") == "VariableDeclaration":
            skip = 1
        elif node.get("name") == indentity and skip == 0:
            return True
        if skip != 1:
            for child_node in node.values():
                occurrence = verify_variable(child_node, indentity)
                if occurrence:
                    return True
    elif isinstance(node, list):
        for child_node in node:
            occurrence = verify_variable(child_node, indentity)
            if occurrence:
                return True
    return False
