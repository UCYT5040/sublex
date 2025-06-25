from sublex.sbx import registry
from sublex.sbx.execute.data import ExecutionData
from sublex.sbx.execute.step import execute_step


async def execute_sbx(sbx_name, *args, **kwargs):
    sbx = registry.get_sbx(sbx_name)
    if not sbx:
        raise ValueError(f"SBX '{sbx_name}' not found.")

    data = ExecutionData()
    for step in sbx.get('steps', []):
        execute_step(data, step)

    return data.result
