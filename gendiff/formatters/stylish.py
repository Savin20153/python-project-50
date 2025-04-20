def format_stylish(diff, indent=0):
    lines = []
    space = '    ' * indent

    for key, node in diff.items():
        node_type = node.get('type')

        if node_type == 'nested':
            lines.append(f"{space}    {key}: {{")
            lines.append(format_stylish(node['children'], indent + 1))
            lines.append(f"{space}    }}")
        elif node_type == 'changed':
            old = stringify(node['old_value'], indent + 1)
            new = stringify(node['new_value'], indent + 1)
            lines.append(f"{space}  - {key}: {old}")
            lines.append(f"{space}  + {key}: {new}")
        elif node_type == 'unchanged':
            val = stringify(node['value'], indent + 1)
            lines.append(f"{space}    {key}: {val}")
        elif node_type == 'added':
            val = stringify(node['value'], indent + 1)
            lines.append(f"{space}  + {key}: {val}")
        elif node_type == 'removed':
            val = stringify(node['value'], indent + 1)
            lines.append(f"{space}  - {key}: {val}")

    if indent == 0:
        return '{\n' + '\n'.join(lines) + '\n}'
    return '\n'.join(lines)


def stringify(value, indent):
    if isinstance(value, dict):
        lines = ['{']
        inner_space = '    ' * indent
        for k, v in value.items():
            lines.append(f"{inner_space}    {k}: {stringify(v, indent + 1)}")
        lines.append(f"{'    ' * (indent - 1)}    }}")
        return '\n'.join(lines)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif value == '':  
        return ''
    return str(value)