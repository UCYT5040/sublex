from .interface import Interface
from ..parser import deep_table_to_dict

def execute_sbx(sbx, filters):
    return [deep_table_to_dict(result) for result in dict(sbx["execute"](Interface(sbx), filters)).values()]
