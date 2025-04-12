def format_stylish(diff, indent=0):
    lines = []
    space = '    ' * indent
    
    for key, node in diff.items():
        node_type = node['type']
        
        if node_type == 'nested':
            lines.append(f"{space}    {key}: {{")
            lines.append(format_stylish(node['value'], indent + 1))
            lines.append(f"{space}    }}")
        elif node_type == 'changed':
            lines.append(f"{space}  - {key}: {node['old']}")
            lines.append(f"{space}  + {key}: {node['new']}")
        elif node_type == 'unchanged':
            lines.append(f"{space}    {key}: {node['value']}")
        elif node_type == 'added':
            lines.append(f"{space}  + {key}: {node['value']}")
        elif node_type == 'removed':
            lines.append(f"{space}  - {key}: {node['value']}")
    
    return '\n'.join(lines)