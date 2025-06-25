from .data import ExecutionData
from .steps import STEPS


def execute_step(
        execution_data: ExecutionData,
        step: dict
):
    result = STEPS[step['type']](execution_data, step) or {}
    store = step.get('store', None)
    if store:
        store_as = store.get('as', None)
        if store_as:
            execution_data.data[store_as] = {}
            for key, value in store.get('data', {}).items():
                execution_data.data[store_as][key] = result.get(value, None)
        else:
            raise ValueError(f"Store 'as' field is required in step: {step}")
    execution_data.step_completed()
