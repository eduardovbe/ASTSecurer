def find_block_properties(node):
    occurrences = []
    if isinstance(node, dict):
        if node.get("type") == "VariableDeclaration":
            if node.get("typeName").get("type") == "ElementaryTypeName" and node.get("typeName").get("name") in ("uint", "uint256", "uint8"):
                if node.get("expression") is not None:
                    if node.get("expression").get("type") == "MemberAccess":
                        if node.get("expression").get("memberName") in ("timestamp", "number") and node.get("expression").get("expression").get("name") == "block":
                            occurrences.append(f"block.{node.get('expression').get('memberName')}")
        elif node.get("type") == "Assignment":
            if node.get("left").get("type") == "MemberAccess":
                if node.get("left").get("memberName") in ("timestamp", "number") and node.get("left").get("expression").get("name") == "block":
                    occurrences.append(f"block.{node.get('left').get('memberName')}")
        elif node.get("type") == "BinaryOperation":
            left_operand = node.get("left")
            right_operand = node.get("right")
            if left_operand.get("type") == "MemberAccess" and left_operand.get("expression").get("name") == "block":
                if left_operand.get("memberName") in ("timestamp", "number"):
                    occurrences.append(f"block.{left_operand.get('memberName')}")
            elif right_operand.get("type") == "MemberAccess" and right_operand.get("expression").get("name") == "block":
                if right_operand.get("memberName") in ("timestamp", "number"):
                    occurrences.append(f"block.{right_operand.get('memberName')}")
        for child_node in node.values():
            occurrences += find_block_properties(child_node)
    elif isinstance(node, list):
        for child_node in node:
            occurrences += find_block_properties(child_node)
    return occurrences