from typing import Union

from yaml import safe_load, safe_dump


class ConfigItem:
    def __init__(self, name: str, default: any = None, comment: str | None = None):
        self.name = name
        self.value = default
        self.default = default
        self.comment = comment

    def __repr__(self):
        return f"ConfigItem(name={self.name}, value={self.value})"

    def from_dict(self, data: dict):
        self.name = data.get("name")
        self.value = data.get("value")
        self.default = data.get("default")
        self.comment = data.get("comment")

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "value": self.value,
            "default": self.default,
            "comment": self.comment,
        }


class ConfigGroup:
    def __init__(self, name: str, items: list[Union[ConfigItem, "ConfigGroup"]]):
        self.name = name
        self.items = {item.name: item for item in items}

    def add_item(self, item: Union["ConfigItem", "ConfigGroup"]):
        self.items[item.name] = item

    def add_items(self, *items: Union["ConfigItem", "ConfigGroup"]):
        for item in items:
            self.add_item(item)

    def remove_item(self, item_name: str):
        self.items.pop(item_name, None)

    def get_item(self, item_name: str) -> Union["ConfigItem", "ConfigGroup", None]:
        return self.items.get(item_name)

    def __repr__(self):
        return f"ConfigGroup(name={self.name}, items={list(self.items.values())})"

    def from_dict(self, data: dict):
        self.name = data.get("name")
        items_data = data.get(self.name, {})
        self.items = {
            name: self._create_item(name, item_data)
            for name, item_data in items_data.items()
        }

    def to_dict(self, skip_name: bool = False) -> dict:
        items_dict = {name: item.to_dict() for name, item in self.items.items()}
        if skip_name:
            return items_dict
        return {self.name: items_dict}


CONFIG_PATH = "config.yaml"


class Config(ConfigGroup):
    def save(self, path: str = CONFIG_PATH):
        with open(path, "w") as file:
            safe_dump(self.to_dict(), file)

    def load(self, path: str = CONFIG_PATH):
        try:
            with open(path, "r") as file:
                data = safe_load(file)
                self.from_dict(data)
        except FileNotFoundError:
            print(f"Config file {path} not found. Using default configuration.")

    def to_dict(self, skip_name: bool = True) -> dict:
        return super().to_dict(skip_name=skip_name)


config = Config(name="SublexConfig", items=[])
config.load()
