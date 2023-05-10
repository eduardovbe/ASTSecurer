def find_rtl_override_control_character(node):
    # Verificar se o nó é uma atribuição
    if isinstance(node, dict):
        if node.get("type") == "Assignment":
            # Verificar se o lado esquerdo da atribuição é um estado
            if node.get("left").get("type") == "Identifier":
                # Verificar se o lado direito da atribuição contém o control character U+202E
                if "\u202e" in node.get("right").get("src"):
                    return True
        for child_node in node.values():
           if find_rtl_override_control_character(child_node):
               return True
    elif isinstance(node, list):
        for child_node in node:
            if find_rtl_override_control_character(child_node):
                return True
    return False