def find_assembly(node):
    assembly = []
    if isinstance(node, dict) and node.get('type') == "AssemblyExpression":
        function_name = node.get("functionName")
        assembly.append(function_name)
    for key, value in node.items():
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    assembly.extend(find_assembly(item))
        elif isinstance(value, dict):
            assembly.extend(find_assembly(value))
    return assembly