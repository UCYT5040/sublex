import lupa

def deep_table_to_dict(lua_table):
    # Recursively convert Lua table to Python dictionary
    # List support is not imporant since dict with numeric keys is equiv. to a list
    if "LuaTable" in str(type(lua_table)): # TODO: Use a more robust check
        return {k: deep_table_to_dict(v) for k, v in lua_table.items()}
    elif isinstance(lua_table, dict):
        return {key: deep_table_to_dict(value) for key, value in lua_table.items()}
    else:
        return lua_table

def filter_attribute_access(obj, attr_name, is_setting):
    if isinstance(attr_name, str):
        if not attr_name.startswith('_'):
            return attr_name
    raise AttributeError('access denied')

def create_lua_environment():
    

    lua = lupa.LuaRuntime(
        register_eval=False, # type: ignore
        attribute_filter=filter_attribute_access, # type: ignore
        )
    
    return lua


def parse_sbx(content: str):
    lua = create_lua_environment()

    lua.execute(content)

    raw_data: dict = deep_table_to_dict(lua.eval("sublex_data")) # type: ignore
    data = {
        "name": raw_data.get("name", ""),
        "description": raw_data.get("description", ""),
        "version": raw_data.get("version", ""),
        "author": raw_data.get("author", ""),
        "tags": raw_data.get("tags", {}).values(),
    }

    if "supported_filters" not in raw_data:
        raise ValueError("Missing 'supported_filters' in the SBX file")
    
    # TODO: Remove leftover type conversions from before deep_table_to_dict
    data["supported_filters"] = { # TODO: Validate this more thoroughly
        filter_name: dict(aliases).values()
        for filter_name, aliases in dict(raw_data["supported_filters"]).items()
    }

    data["execute"] = lua.eval("sublex_execute")
    data["lua"] = lua  # Store the Lua instance for later use

    # TODO: Implement permissions

    return data
