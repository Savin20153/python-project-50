def build_diff(data1, data2):
    diff = {}
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    
    for key in all_keys:
        if key in data1 and key in data2:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                diff[key] = {
                    'type': 'nested',
                    'value': build_diff(data1[key], data2[key])
                }
            elif data1[key] == data2[key]:
                diff[key] = {
                    'type': 'unchanged',
                    'value': data1[key]
                }
            else:
                diff[key] = {
                    'type': 'changed',
                    'old': data1[key],
                    'new': data2[key]
                }
        elif key in data1:
            diff[key] = {
                'type': 'removed',
                'value': data1[key]
            }
        else:
            diff[key] = {
                'type': 'added',
                'value': data2[key]
            }
    return diff