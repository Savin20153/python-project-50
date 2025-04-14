def stringify_value(value):
    if isinstance(value, (dict, list)):
        return "[complex value]"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def format_plain(diff, parent_key=''):
    lines = []
    for key, node in diff.items():
        current_key = f"{parent_key}.{key}" if parent_key else key
        node_type = node.get('type')

        if node_type == 'nested':
            lines.append(format_plain(node['children'], current_key))
        elif node_type == 'changed':
            old = stringify_value(node.get('old_value'))
            new = stringify_value(node.get('new_value'))
            msg = f"Property '{current_key}' was updated. From {old} to {new}"
            lines.append(msg)
        elif node_type == 'added':
            value = stringify_value(node.get('value'))
            msg = f"Property '{current_key}' was added with value: {value}"
            lines.append(msg)
        elif node_type == 'removed':
            lines.append(f"Property '{current_key}' was removed")
    
    return '\n'.join(lines)