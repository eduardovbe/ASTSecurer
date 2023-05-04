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