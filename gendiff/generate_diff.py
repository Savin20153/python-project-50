def generate_diff(first_file, second_file):
    result_diff = {}
    all_keys = sorted(set(first_file.keys()) | set(second_file.keys()))

    for key in all_keys:
        if key in first_file and key in second_file:
            if first_file[key] == second_file[key]:
                result_diff[f'  {key}'] = first_file[key]
            else:
                result_diff[f'- {key}'] = first_file[key]
                result_diff[f'+ {key}'] = second_file[key]
        elif key in first_file:
            result_diff[f'- {key}'] = first_file[key]
        else:
            result_diff[f'+ {key}'] = second_file[key]

    return result_diff  