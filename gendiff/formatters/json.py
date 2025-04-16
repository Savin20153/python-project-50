import json


def format_json(diff):
    def walk(node):
        if not isinstance(node, dict):
            return node
        
        result = {}
        for key, data in node.items():
            if not isinstance(data, dict):
                result[key] = data
                continue
                
            if data.get('type') == 'nested':
                result[key] = walk(data.get('children', {}))
            elif data.get('type') == 'changed':
                result[key] = {
                    'type': 'changed',
                    'old_value': walk(data.get('old_value')),
                    'new_value': walk(data.get('new_value'))
                }
            else:
                result[key] = {
                    'type': data.get('type'),
                    'value': walk(data.get('value'))
                }
        return result
    
    return json.dumps(walk(diff), indent=2)