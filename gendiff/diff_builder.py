def build_diff(data1, data2):
    diff = {}
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    for key in all_keys:
        # Оба значения существуют
        if key in data1 and key in data2:
            value1 = data1[key]
            value2 = data2[key]

            # Если оба значения — словари, рекурсивно сравниваем их
            if isinstance(value1, dict) and isinstance(value2, dict):
                diff[key] = {
                    'type': 'nested',
                    'children': build_diff(value1, value2)
                }
            # Если значения разные
            elif value1 != value2:
                diff[key] = {
                    'type': 'changed',
                    'old_value': value1,
                    'new_value': value2
                }
            # Если значения одинаковые
            else:
                diff[key] = {
                    'type': 'unchanged',
                    'value': value1
                }

        # Ключ только в первом файле (удален)
        elif key in data1:
            diff[key] = {
                'type': 'removed',
                'value': data1[key]
            }

        # Ключ только во втором файле (добавлен)
        else:
            diff[key] = {
                'type': 'added',
                'value': data2[key]
            }

    return diff