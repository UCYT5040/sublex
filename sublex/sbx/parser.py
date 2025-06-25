import yaml

def parse_sbx(yaml_content):
    try:
        data = yaml.safe_load(yaml_content)
        required_fields = ['name', 'description', 'version', 'tags', 'filters']
        sbx_info = {field: data.get(field) for field in required_fields}
        if not all(sbx_info.values()):
            return None
        return sbx_info
    except Exception:  # TODO: Make exception clause less broad
        return None

