import os
from . import parser, registry
from ..config import config

SBX_DIRECTORY = config.get_item('sbx').get_item('path').value

def load():
    sbx_files = [f for f in os.listdir(SBX_DIRECTORY) if f.endswith('.yaml') or f.endswith('.yml')]
    for filename in sbx_files:
        path = os.path.join(SBX_DIRECTORY, filename)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            sbx_data = parser.parse_sbx(content)
            if sbx_data:
                registry.register_sbx(filename, sbx_data)
        except Exception:
            pass
