import json


def format_json(diff):
    def walk(node):
        if isinstance(node, dict) and 'type' in node:
            if node['type'] == 'nested':
                return {
                    'type': 'nested',
                    'value': walk(node['children'])
                }
            elif node['type'] == 'changed':
                return {
                    'type': 'changed',
                    'old_value': walk(node['old_value']),
                    'new_value': walk(node['new_value'])
                }
            else:
                return {
                    'type': node['type'],
                    'value': walk(node['value'])
                }
        elif isinstance(node, dict):
            return {k: walk(v) for k, v in node.items()}
        elif isinstance(node, list):
            return [walk(item) for item in node]
        else:
            return node
    
    return json.dumps(walk(diff), indent=4)