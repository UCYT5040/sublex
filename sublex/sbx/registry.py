_sbx_registry = {}


def register_sbx(filename, sbx_data):
    _sbx_registry[filename] = sbx_data


def get_all():
    return list(_sbx_registry.values())


def get_by_name(name):
    for sbx in _sbx_registry.values():
        if sbx.get("name") == name:
            return sbx
    return None
