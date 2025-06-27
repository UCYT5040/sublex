import os

from . import parser, registry
from ..config import config, ConfigGroup, ConfigItem

SBX_CONFIG = config.get_item("sbx")
if not SBX_CONFIG or not isinstance(SBX_CONFIG, ConfigGroup):
    raise ValueError("SBX configuration not found in the config file.")
SBX_DIRECTORY_ITEM = SBX_CONFIG.get_item("path")
if not SBX_DIRECTORY_ITEM or not isinstance(SBX_DIRECTORY_ITEM, ConfigItem):
    raise ValueError("SBX directory path not found in the config file.")
SBX_DIRECTORY = SBX_DIRECTORY_ITEM.value


def load():
    sbx_files = [
        f
        for f in os.listdir(SBX_DIRECTORY)
        if f.endswith(".sbx") or f.endswith(".lua")
    ]
    for filename in sbx_files:
        path = os.path.join(SBX_DIRECTORY, filename)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        sbx_data = parser.parse_sbx(content)
        if sbx_data:
            registry.register_sbx(filename, sbx_data)
        else:
            print(
                f"Failed to parse SBX file: {filename}. Please check the file format."
            )
