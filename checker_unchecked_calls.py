def find_unchecked_calls(node, find=0):
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
            if node['expression']['expression'].get("name") is not None:
                unchecked_calls.append(node['expression']['expression'].get("name"))
        for key, value in node.items():
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        unchecked_calls.extend(find_unchecked_calls(item, find=find))
            elif isinstance(value, dict):
                unchecked_calls.extend(find_unchecked_calls(value, find=find))
        return unchecked_calls
    except:
        pass