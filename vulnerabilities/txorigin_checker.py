import json
from abstract_tree.ast_generator import *

def ast_load():
    with open('ast.json', 'r') as f:
        data = f.read()
    return json.loads(data)


def find_tx_origin(node):
    occurrences = []
    try:
        if isinstance(node, dict):
            if node.get("type") == "BinaryOperation" and node.get("operator") == "==":
                if node.get("left").get("type") == "MemberAccess" and node.get("left").get("memberName") == "origin" and node.get("left").get("expression").get("name") == "tx":
                    ast = ast_load()
                    if verify_msgsender(ast, node.get("right").get("name")):
                        occurrences.append(f"tx.origin == {node.get('right').get('name')}")
                elif node.get("right").get("type") == "MemberAccess" and node.get("right").get(
                        "memberName") == "origin" and node.get("right").get("expression").get("name") == "tx":
                    ast = ast_load()
                    if verify_msgsender(ast, node.get("left").get("name")):
                        occurrences.append(f"{node.get('left').get('name')} == tx.origin")
            for child_node in node.values():
                occurrences += find_tx_origin(child_node)
        elif isinstance(node, list):
            for child_node in node:
                occurrences += find_tx_origin(child_node)
        return occurrences
    except:
        pass

def verify_msgsender(node, indentity):
    if isinstance(node, dict):
        if node.get("type") == "BinaryOperation" and node.get("operator") == "=":
            if node.get("left").get("type") == "Identifier" and node.get("left").get("name") == indentity and node.get("right").get("expression").get("name") == "msg"\
                    and node.get("right").get("memberName") == "sender":
                return True
        for child_node in node.values():
            occurrence = verify_msgsender(child_node, indentity)
            if occurrence:
                return True
    elif isinstance(node, list):
        for child_node in node:
            occurrence = verify_msgsender(child_node, indentity)
            if occurrence:
                return True
    return False
