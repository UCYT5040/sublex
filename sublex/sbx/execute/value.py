VALUE_TYPES = [
    'const',
    'variable'
]


def execute_value(value, execution_data) -> any:
    if value['type'] == 'const':
        return value['value']
    elif value['type'] == 'variable':
        data = None
        for path in value['path']:
            if data is None:
                data = execution_data.data.get(path)
            else:
                data = data.get(path)
        if data is None:
            raise ValueError(f"Variable path '{value['path']}' not found in execution data.")
        return data
    else:
        raise ValueError(f"Unknown value type '{value['type']}' in value: {value}")
