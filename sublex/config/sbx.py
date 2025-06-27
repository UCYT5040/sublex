from . import config, ConfigItem, ConfigGroup


def initialize():
    config.add_items(
        ConfigGroup(
            name="sbx",
            items=[
                ConfigItem(
                    name="path",
                    default="sbx",
                    comment="All files in this directory and its subdirectories will be loaded as SBX files."
                )
            ]
        )
    )
