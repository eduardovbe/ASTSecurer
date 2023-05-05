def find_block_properties(node):
    occurrences = []
    if isinstance(node, dict):
        if node.get("type") == "VariableDeclaration":
            if node.get("typeName").get("type") == "ElementaryTypeName" and node.get("typeName").get("name") in ("uint", "uint256", "uint8"):
                if node.get("expression") is not None:
                    if node.get("expression").get("type") == "MemberAccess":
                        if node.get("expression").get("member") in ("timestamp", "number") and node.get("expression").get("expression").get("name") == "block":
                            occurrences.append(node)
        elif node.get("type") == "Assignment":
            if node.get("left").get("type") == "MemberAccess":
                if node.get("left").get("member") in ("timestamp", "number") and node.get("left").get("expression").get("name") == "block":
                    occurrences.append(node)
        for child_node in node.values():
            occurrences += find_block_properties(child_node)
    elif isinstance(node, list):
        for child_node in node:
            occurrences += find_block_properties(child_node)
    return occurrences