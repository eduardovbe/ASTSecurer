import re

def find_rtl_override_control_character(node):
    # Verificar se o nó é uma atribuição

    if isinstance(node, dict):
        if node.get("initialValue") is not None:
            if node.get("initialValue").get("value") is not None:
                if re.search(r"\\u202E", node.get("initialValue").get("value")):
                    return True
        for child_node in node.values():
           if find_rtl_override_control_character(child_node):
               return True
    elif isinstance(node, list):
        for child_node in node:
            if find_rtl_override_control_character(child_node):
                return True
    return False