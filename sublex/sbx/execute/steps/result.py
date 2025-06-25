from sublex.sbx.execute.data import ExecutionData
from sublex.sbx.execute.value import execute_value


def result_step(execution_data: ExecutionData, step: dict):
    result_name = execute_value(step['name'])
    result_link = step.get('link', None)
    other_result_data = {}
    for other_result in step.get('other', []):
        other_result_value = execute_value(other_result['value'], execution_data)
        other_result_data[other_result['name']] = other_result_value
    execution_data.result = {
        'name': result_name,
        'link': result_link,
        'other': other_result_data
    }
